@echo off
set SDK=C:\Users\joaov\Downloads\renpy-8.5.3-sdk
set PROJETO=%SDK%\vn-engine\VnGame
set DISTS=%SDK%\vn-engine\VnGame-1.0-dists
set BUTLER=%SDK%\vn-engine\butler-windows-amd64\butler.exe
set ITCH_PROJETO=limerenceofc/limerence

echo ============================
echo  Buildando o jogo...
echo ============================
"%SDK%\renpy.exe" "%PROJETO%" distribute

if not exist "%DISTS%\VnGame-1.0-win.zip" (
    echo ERRO: nao achei o zip do Windows em %DISTS%
    echo Confere se o build terminou sem erro acima.
    pause
    exit /b 1
)

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
echo  Pronto! Tudo buildado e subido.
echo ============================
pause