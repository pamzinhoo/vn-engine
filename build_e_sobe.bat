@echo off
setlocal enabledelayedexpansion

set SDK=C:\Users\joaov\Downloads\renpy-8.5.3-sdk
set PROJETO=%SDK%\vn-engine\VnGame
set DISTS=%SDK%\vn-engine\VnGame-1.0-dists
set BUTLER=%SDK%\vn-engine\butler-windows-amd64\butler.exe
set ITCH_PROJETO=limerenceofc/limerence

REM renpy.exe e GUI-subsystem: o cmd dispara e NAO espera terminar, entao o
REM script seguia para o upload antes do build existir. python.exe do proprio
REM SDK e console-subsystem, bloqueia ate o fim e ainda mostra o progresso.
set PY=%SDK%\lib\py3-windows-x86_64\python.exe

if not exist "%PY%" (
    echo ERRO: nao achei o python do SDK em %PY%
    pause
    exit /b 1
)

echo ============================
echo  O que voce quer buildar e subir?
echo ============================
echo  1 - Windows
echo  2 - Mac
echo  3 - Linux
echo  4 - Mobile (Android)
echo  5 - Todos
echo ============================
set /p ESCOLHA="Digite o numero: "

set DO_WIN=0
set DO_MAC=0
set DO_LINUX=0
set DO_MOBILE=0

if "%ESCOLHA%"=="1" set DO_WIN=1
if "%ESCOLHA%"=="2" set DO_MAC=1
if "%ESCOLHA%"=="3" set DO_LINUX=1
if "%ESCOLHA%"=="4" set DO_MOBILE=1
if "%ESCOLHA%"=="5" set DO_WIN=1
if "%ESCOLHA%"=="5" set DO_MAC=1
if "%ESCOLHA%"=="5" set DO_LINUX=1
if "%ESCOLHA%"=="5" set DO_MOBILE=1

if "%DO_WIN%%DO_MAC%%DO_LINUX%%DO_MOBILE%"=="0000" (
    echo ERRO: opcao invalida "%ESCOLHA%".
    pause
    exit /b 1
)

REM ---- builds ----

if not "%DO_WIN%"=="1" goto skip_build_win
echo ============================
echo  Buildando Windows...
echo ============================
"%PY%" "%SDK%\renpy.py" "%SDK%\launcher" distribute "%PROJETO%" --dest "%DISTS%" --package win
if errorlevel 1 (
    echo ERRO: o build do Windows falhou.
    pause
    exit /b 1
)
:skip_build_win

if not "%DO_MAC%"=="1" goto skip_build_mac
echo ============================
echo  Buildando Mac...
echo ============================
"%PY%" "%SDK%\renpy.py" "%SDK%\launcher" distribute "%PROJETO%" --dest "%DISTS%" --package mac
if errorlevel 1 (
    echo ERRO: o build do Mac falhou.
    pause
    exit /b 1
)
:skip_build_mac

if not "%DO_LINUX%"=="1" goto skip_build_linux
echo ============================
echo  Buildando Linux...
echo ============================
"%PY%" "%SDK%\renpy.py" "%SDK%\launcher" distribute "%PROJETO%" --dest "%DISTS%" --package linux
if errorlevel 1 (
    echo ERRO: o build do Linux falhou.
    pause
    exit /b 1
)
:skip_build_linux

if not "%DO_MOBILE%"=="1" goto skip_build_mobile
echo ============================
echo  Buildando Android (APK)...
echo ============================
REM Apaga APK antigo para nao subir build velho caso este falhe.
del /q "%DISTS%\*-release.apk" 2>nul
"%PY%" "%SDK%\renpy.py" "%SDK%\launcher" android_build "%PROJETO%" --dest "%DISTS%"
if errorlevel 1 (
    echo ERRO: o build do Android falhou.
    pause
    exit /b 1
)

REM O nome do APK carrega um timestamp, entao pega o mais recente por glob.
set "APK="
for /f "delims=" %%f in ('dir /b /o-d "%DISTS%\*-release.apk" 2^>nul') do (
    if not defined APK set "APK=%DISTS%\%%f"
)
if not defined APK (
    echo ERRO: nao achei nenhum *-release.apk em %DISTS%
    pause
    exit /b 1
)
echo APK: !APK!

REM O itch mostra o nome do arquivo enviado. O APK do Ren'Py carrega
REM package e timestamp, entao copia para um nome fixo antes do push.
set "APK_UPLOAD=%DISTS%\limerence-android.apk"
copy /y "!APK!" "!APK_UPLOAD!" >nul
if errorlevel 1 (
    echo ERRO: nao consegui copiar o APK para !APK_UPLOAD!
    pause
    exit /b 1
)
:skip_build_mobile

REM ---- uploads ----

if not "%DO_WIN%"=="1" goto skip_push_win
if not exist "%DISTS%\VnGame-1.0-win.zip" (
    echo ERRO: nao achei o zip do Windows em %DISTS%
    pause
    exit /b 1
)
echo ============================
echo  Subindo Windows...
echo ============================
"%BUTLER%" push "%DISTS%\VnGame-1.0-win.zip" %ITCH_PROJETO%:windows
:skip_push_win

if not "%DO_MAC%"=="1" goto skip_push_mac
echo ============================
echo  Subindo Mac...
echo ============================
"%BUTLER%" push "%DISTS%\VnGame-1.0-mac.zip" %ITCH_PROJETO%:mac
:skip_push_mac

if not "%DO_LINUX%"=="1" goto skip_push_linux
echo ============================
echo  Subindo Linux...
echo ============================
"%BUTLER%" push "%DISTS%\VnGame-1.0-linux.tar.bz2" %ITCH_PROJETO%:linux
:skip_push_linux

if not "%DO_MOBILE%"=="1" goto skip_push_mobile
echo ============================
echo  Subindo Android...
echo ============================
"%BUTLER%" push "!APK_UPLOAD!" %ITCH_PROJETO%:android
:skip_push_mobile

echo ============================
echo  Pronto! Build(s) selecionado(s) buildado(s) e subido(s).
echo ============================
pause
