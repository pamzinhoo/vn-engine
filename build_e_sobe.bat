@echo off
setlocal enabledelayedexpansion

set SDK=C:\Users\joaov\Downloads\renpy-8.5.3-sdk
set PROJETO=%SDK%\vn-engine\VnGame
set DISTS=%SDK%\vn-engine\VnGame-1.0-dists
set BUTLER=%SDK%\vn-engine\butler-windows-amd64\butler.exe
set ITCH_PROJETO=limerenceofc/limerence

echo ============================
echo  Buildando desktop...
echo ============================
"%SDK%\renpy.exe" "%PROJETO%" distribute

if not exist "%DISTS%\VnGame-1.0-win.zip" (
    echo ERRO: nao achei o zip do Windows em %DISTS%
    echo Confere se o build terminou sem erro acima.
    pause
    exit /b 1
)

echo ============================
echo  Buildando Android (APK)...
echo ============================
REM Apaga APK antigo para nao subir build velho caso este falhe.
del /q "%DISTS%\*-release.apk" 2>nul
"%SDK%\renpy.exe" launcher android_build "%PROJETO%" --dest "%DISTS%"

REM O nome do APK carrega um timestamp, entao pega o mais recente por glob.
set "APK="
for /f "delims=" %%f in ('dir /b /o-d "%DISTS%\*-release.apk" 2^>nul') do (
    if not defined APK set "APK=%DISTS%\%%f"
)
if not defined APK (
    echo ERRO: nao achei nenhum *-release.apk em %DISTS%
    echo Confere se o build do Android terminou sem erro acima.
    pause
    exit /b 1
)
echo APK: !APK!

echo ============================
echo  Subindo Windows...
echo ============================
"%BUTLER%" push "%DISTS%\VnGame-1.0-win.zip" %ITCH_PROJETO%:windows

echo ============================
echo  Subindo Mac...
echo ============================
"%BUTLER%" push "%DISTS%\VnGame-1.0-mac.zip" %ITCH_PROJETO%:mac

echo ============================
echo  Subindo Linux...
echo ============================
"%BUTLER%" push "%DISTS%\VnGame-1.0-linux.tar.bz2" %ITCH_PROJETO%:linux

echo ============================
echo  Subindo Android...
echo ============================
"%BUTLER%" push "!APK!" %ITCH_PROJETO%:android

echo ============================
echo  Pronto! Tudo buildado e subido.
echo ============================
pause
