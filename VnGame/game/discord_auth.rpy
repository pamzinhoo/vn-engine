# ============================================================================
# Login com Discord (device flow) contra o backend Limerence.
# Backend: https://limerence-backend.onrender.com (ver backend/api/routes/auth_routes.py)
# ============================================================================

init -10 python:
    import json
    import os as _os
    import platform
    import ssl
    import threading
    import time as _time
    import urllib.request
    import urllib.error
    import uuid as _uuid
    import webbrowser

    def _discord_open_browser(url):
        """Abre o navegador padrao ja em primeiro plano. webbrowser.open()
        sozinho as vezes abre a aba atras da janela fullscreen do Ren'Py no
        Windows; os.startfile (ShellExecute) traz a janela do navegador pra
        frente de verdade.

        Corrigido em 2026-08-22: no Android/iOS, webbrowser.open() nao tem
        navegador registrado pra abrir e falha silenciosamente (excecao
        engolida abaixo) -- o jogador nunca via a tela de login, e o app
        ficava preso pra sempre em "Conectando com o Discord..." esperando
        uma confirmacao que nunca chegava. renpy.open_url() e' a API do
        proprio Ren'Py pra isso, funciona via Intent no Android/iOS."""
        if platform.system() == "Windows":
            try:
                _os.startfile(url)
                return
            except Exception:
                pass
        if getattr(renpy, "android", False) or getattr(renpy, "ios", False):
            try:
                renpy.open_url(url)
                return
            except Exception:
                pass
        try:
            webbrowser.open(url, new=2)
        except Exception:
            pass

    DISCORD_AUTH_BACKEND_URL = "https://limerence-backend.onrender.com"

    def _discord_ssl_context():
        """Python embutido do Ren'Py SDK as vezes nao enxerga a lista de CAs
        do sistema. Tenta usar certifi (se empacotado); se nao der, cai pro
        contexto padrao do sistema; em ultimo caso, segue sem verificar
        (evita travar o login por causa disso, backend e https conhecido)."""
        try:
            import certifi
            return ssl.create_default_context(cafile=certifi.where())
        except Exception:
            pass
        try:
            return ssl.create_default_context()
        except Exception:
            pass
        ctx = ssl._create_unverified_context()
        return ctx

    _DISCORD_SSL_CONTEXT = _discord_ssl_context()

    class DiscordAuthState(object):
        """Estado compartilhado entre a thread de rede e a UI (thread principal)."""

        def __init__(self):
            self.reset()

        def reset(self):
            self.status = "idle"          # idle | starting | waiting_browser | polling | success | error | expired | denied
            self.message = ""
            self.verification_uri = None
            self.user_code = None
            self.device_code = None
            self.interval = 5
            self.error = None

    discord_auth_state = DiscordAuthState()

    class DiscordVerifiedState(object):
        """Estado da checagem AO VIVO de 'ainda tenho o cargo Verificado?'
        (ver backend GET /player/verified). Deliberadamente SEPARADO de
        `persistent.discord_access_token` -- ter um token salvo so prova que
        o jogador logou uma vez, nao que o cargo continua valido agora.
        `verified` comeca em False (bloqueado) e so vira True depois de uma
        resposta POSITIVA e recente do backend -- nunca assume liberado por
        padrao (fail-closed)."""

        def __init__(self):
            self.verified = False
            self.checking = False
            self.last_checked_at = 0.0
            self.last_error = None

    discord_verified_state = DiscordVerifiedState()

    def _discord_device_uuid():
        """UUID estavel por instalacao, guardado no persistent do Ren'Py."""
        if not persistent.discord_device_uuid:
            persistent.discord_device_uuid = str(_uuid.uuid4())
        return persistent.discord_device_uuid

    def _discord_http_json(path, payload, timeout=15):
        url = DISCORD_AUTH_BACKEND_URL + path
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url, data=data, method="POST",
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=_DISCORD_SSL_CONTEXT) as resp:
                body = resp.read().decode("utf-8")
                return json.loads(body), None
        except urllib.error.HTTPError as exc:
            try:
                body = json.loads(exc.read().decode("utf-8"))
                msg = body.get("detail", {}).get("message", str(exc))
            except Exception:
                msg = str(exc)
            return None, msg
        except Exception as exc:
            return None, str(exc)

    def _discord_http_post_json(path, payload, timeout=15):
        """Igual _discord_http_json, mas devolve tambem o status code --
        usado por _discord_refresh_tokens pra distinguir falha definitiva
        (401/403, refresh_token morto de vez) de falha transitoria (rede/5xx,
        onde vale tentar de novo depois sem forcar o jogador a logar de novo)."""
        url = DISCORD_AUTH_BACKEND_URL + path
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url, data=data, method="POST",
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=_DISCORD_SSL_CONTEXT) as resp:
                body = resp.read().decode("utf-8")
                return resp.status, json.loads(body), None
        except urllib.error.HTTPError as exc:
            try:
                body = json.loads(exc.read().decode("utf-8"))
                msg = body.get("detail", {}).get("message", str(exc))
            except Exception:
                msg = str(exc)
            return exc.code, None, msg
        except Exception as exc:
            return None, None, str(exc)

    def _discord_refresh_tokens():
        """Troca o refresh_token salvo por um par (access+refresh) novo, sem
        passar pelo device flow de novo -- e' o que permite ficar 'logado'
        por ate 30 dias (refresh_token_ttl_days) mesmo o access_token
        expirando a cada 15min (jwt_access_ttl_seconds).
        Retorna True se renovou. Retorna False em falha transitoria (rede/5xx)
        SEM apagar os tokens salvos (vale tentar de novo depois). So apaga os
        tokens (forcando login manual de novo) quando o backend confirma de
        vez que a sessao morreu (401/403 -- refresh_token invalido, expirado,
        revogado ou reuso detectado)."""
        refresh_token = persistent.discord_refresh_token
        if not refresh_token:
            return False
        payload = {"refresh_token": refresh_token, "device_uuid": _discord_device_uuid()}
        status_code, data, err = _discord_http_post_json("/auth/refresh", payload)
        if status_code in (401, 403):
            persistent.discord_access_token = None
            persistent.discord_refresh_token = None
            return False
        if err or not data:
            return False
        persistent.discord_access_token = data["access_token"]
        persistent.discord_refresh_token = data["refresh_token"]
        return True

    def _discord_http_get_json(path, access_token, timeout=10):
        """GET autenticado (Authorization: Bearer <token>) contra o backend.
        Devolve (status_code, data_ou_None, erro_ou_None) -- o status code
        importa aqui (em especial 401, ver refresh_discord_verified_status)
        de um jeito que _discord_http_json (so usado no login, onde so
        sucesso/erro generico importa) nao precisava expor."""
        url = DISCORD_AUTH_BACKEND_URL + path
        req = urllib.request.Request(
            url, method="GET",
            headers={"Authorization": "Bearer " + access_token},
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=_DISCORD_SSL_CONTEXT) as resp:
                body = resp.read().decode("utf-8")
                return resp.status, json.loads(body), None
        except urllib.error.HTTPError as exc:
            try:
                body = json.loads(exc.read().decode("utf-8"))
                msg = body.get("detail", {}).get("message", str(exc))
            except Exception:
                msg = str(exc)
            return exc.code, None, msg
        except Exception as exc:
            return None, None, str(exc)

    def _discord_login_worker():
        state = discord_auth_state
        state.status = "starting"

        payload = {
            "device_uuid": _discord_device_uuid(),
            "os_info": platform.platform(),
            "launcher_version": config.version,
        }
        data, err = _discord_http_json("/auth/device/code", payload)
        if err or not data:
            state.status = "error"
            state.error = err or "Falha ao iniciar login."
            return

        state.device_code = data["device_code"]
        state.user_code = data["user_code"]
        state.verification_uri = data["verification_uri"]
        state.interval = data.get("interval", 5)
        state.status = "waiting_browser"

        _discord_open_browser(state.verification_uri)

        state.status = "polling"

        import time
        expires_at = time.time() + data.get("expires_in", 600)
        while time.time() < expires_at:
            time.sleep(state.interval)

            poll_data, poll_err = _discord_http_json(
                "/auth/device/token", {"device_code": state.device_code}
            )
            if poll_err:
                # rate limit / erro de rede transitorio: continua tentando
                continue

            poll_status = poll_data.get("status")

            if poll_status == "success":
                persistent.discord_access_token = poll_data["access_token"]
                persistent.discord_refresh_token = poll_data["refresh_token"]
                state.status = "success"
                # Login novo -> checa o cargo verificado ja de cara, sem
                # esperar o proximo timer periodico da tela de selecao (ver
                # screen escolha_genero em script.rpy). O bot concede o
                # cargo de forma assincrona (notify_player_verified, best
                # effort) entao a PRIMEIRA checagem pode ainda vir False por
                # uma corrida de milissegundos -- o timer periodico da tela
                # cobre isso, nao e' um problema de seguranca, so de UX.
                refresh_discord_verified_status()
                return
            elif poll_status == "slow_down":
                state.interval = poll_data.get("interval", state.interval * 2)
            elif poll_status == "access_denied":
                state.status = "denied"
                return
            elif poll_status == "expired_token":
                state.status = "expired"
                return
            # authorization_pending -> continua o loop

        state.status = "expired"

    def start_discord_login():
        if discord_auth_state.status in ("starting", "waiting_browser", "polling"):
            return
        discord_auth_state.reset()
        t = threading.Thread(target=_discord_login_worker, daemon=True)
        t.start()
        renpy.show_screen("discord_login_status")

    def discord_button_action():
        """Mesmo estado ao vivo da carta de DLC (discord_verified_state.verified),
        nao mais discord_is_logged_in() -- token salvo sem cargo valido nao
        conta como "ja vinculado". Assim icone da tela principal e carta do
        meio concordam sempre: os dois levam pro login ate confirmacao
        positiva e recente do backend."""
        if discord_verified_state.verified:
            _discord_open_browser(DISCORD_AUTH_BACKEND_URL + "/auth/discord/already-linked")
        else:
            start_discord_login()

    def discord_logout():
        persistent.discord_access_token = None
        persistent.discord_refresh_token = None
        discord_auth_state.reset()
        discord_verified_state.verified = False
        discord_verified_state.last_checked_at = 0.0
        # Desvincular tranca a DLC de novo -- acesso segue o cargo Verificado
        # em tempo real, nao fica permanente so por ter conectado uma vez.

    def discord_is_logged_in():
        """Prova SO que existe um token salvo localmente -- ISSO NAO SIGNIFICA
        que o jogador ainda tem o cargo Verificado agora. Nao use esta funcao
        pra decidir se libera conteudo que exige o cargo; use
        `discord_verified_state.verified` (ver refresh_discord_verified_status
        logo abaixo), que e' checado ao vivo contra o backend. Esta funcao
        continua existindo so pra decidir se mostra o botao 'Entrar' ou
        'Discord ja vinculado' (discord_button_action) -- uma decisao de UI
        sem risco, nao de autorizacao."""
        return bool(persistent.discord_access_token)

    def _discord_verified_worker():
        state = discord_verified_state
        access_token = persistent.discord_access_token
        if not access_token:
            state.verified = False
            state.checking = False
            return

        try:
            status_code, data, err = _discord_http_get_json("/player/verified", access_token)

            if status_code == 401:
                # Access token expirado (dura so 15min) -- tenta renovar com o
                # refresh_token (dura 30 dias) antes de desistir. So volta pra
                # tela de login se o refresh tambem falhar de vez (401/403 =
                # sessao realmente morta); falha transitoria de rede no
                # refresh mantem os tokens salvos e so bloqueia esta checagem.
                if _discord_refresh_tokens():
                    access_token = persistent.discord_access_token
                    status_code, data, err = _discord_http_get_json("/player/verified", access_token)
                else:
                    state.verified = False
                    state.last_error = "sessao expirada"
                    return

            if status_code == 401:
                # Token novo (pos-refresh) ja voltou 401 -- nao insiste mais
                # nesta rodada, fail-closed.
                state.verified = False
                state.last_error = "sessao expirada"
            elif err or data is None:
                # Falha de rede/bot offline/etc -- FAIL-CLOSED: mantem
                # bloqueado. Nao assume "ainda deve estar verificado" so porque
                # a ultima checagem confirmada foi True; melhor pedir pra
                # tentar de novo do que liberar conteudo sem confirmacao
                # positiva e recente.
                state.verified = False
                state.last_error = err or "resposta vazia do backend"
            else:
                state.verified = bool(data.get("verified", False))
                state.last_error = None
        except Exception as exc:
            # Qualquer excecao inesperada -- fail-closed igual aos outros
            # ramos, e o finally abaixo garante que 'checking' nunca fica
            # travado em True (o que bloquearia toda checagem futura).
            state.verified = False
            state.last_error = str(exc)
        finally:
            state.last_checked_at = _time.time()
            state.checking = False

    def refresh_discord_verified_status():
        """Dispara a checagem ao vivo em background (nunca bloqueia a UI).
        Chamada: (1) logo apos login bem sucedido; (2) periodicamente
        enquanto a tela de selecao de genero esta aberta (ver script.rpy) --
        e' ai' que a carta do meio (DLC) decide se mostra liberada ou
        trancada, sempre em cima de `discord_verified_state.verified`, nunca
        de `discord_is_logged_in()`."""
        if not discord_is_logged_in():
            discord_verified_state.verified = False
            return
        if discord_verified_state.checking:
            return
        discord_verified_state.checking = True
        t = threading.Thread(target=_discord_verified_worker, daemon=True)
        t.start()

init python:

    def dlc_liberada():
        """Unico lugar que decide se a DLC aparece liberada.

        Segue o cargo Verificado em tempo real: `discord_verified_state.verified`
        vem da ultima checagem ao vivo contra o backend (ver
        _discord_verified_worker). Perdeu o cargo ou desvinculou a conta --
        tranca de novo na proxima checagem, nao fica liberado pra sempre so
        por ter conectado uma vez.
        """
        return discord_verified_state.verified

    def precisa_checar_discord():
        """A checagem periodica nunca para -- o acesso pode mudar a qualquer
        momento (desvinculou, perdeu o cargo), entao sempre vale a pena
        confirmar de novo."""
        return True


default persistent.discord_device_uuid = None
default persistent.discord_access_token = None
default persistent.discord_refresh_token = None


## Tela de status do login (spinner / codigo / erro) ##########################
screen discord_login_status():
    modal True
    zorder 200

    add "#000000cc"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        xminimum 520

        vbox:
            spacing 16
            xalign 0.5

            if discord_auth_state.status in ("starting",):
                text _("Conectando com o Discord...") xalign 0.5

            elif discord_auth_state.status in ("waiting_browser", "polling"):
                text _("Confirme o login na aba do navegador que abriu.") xalign 0.5
                if discord_auth_state.user_code:
                    text "[discord_auth_state.user_code!q]" xalign 0.5 size 34
                text _("Aguardando confirmação...") xalign 0.5 size 18

            elif discord_auth_state.status == "success":
                text _("Login concluído!") xalign 0.5
                timer 1.2 action Hide("discord_login_status")

            elif discord_auth_state.status == "denied":
                text _("Login cancelado.") xalign 0.5

            elif discord_auth_state.status == "expired":
                text _("Tempo esgotado, tente novamente.") xalign 0.5

            elif discord_auth_state.status == "error":
                text _("Não foi possível conectar: [discord_auth_state.error!q]") xalign 0.5

            if discord_auth_state.status not in ("starting", "waiting_browser", "polling"):
                textbutton _("Fechar"):
                    xalign 0.5
                    action Hide("discord_login_status")
            else:
                textbutton _("Cancelar"):
                    xalign 0.5
                    action [SetField(discord_auth_state, "status", "denied"), Hide("discord_login_status")]

    ## Repinta a tela periodicamente pra refletir o estado atualizado pela thread.
    timer 0.3 repeat True action Function(renpy.restart_interaction)
