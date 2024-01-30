@echo off
title Menjalankan Perintah Python

REM Memeriksa apakah Python sudah diinstal sebelumnya
python --version > nul 2>&1
if %errorlevel% equ 0 (
    echo Python sudah terinstal. Melanjutkan ke langkah selanjutnya...
) else (
    REM Mengunduh installer Python terbaru
    echo Mengunduh installer Python terbaru...
    powershell -Command "& {Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe -OutFile python_installer.exe}"

    REM Memeriksa apakah pengunduhan berhasil
    if not exist python_installer.exe (
        echo Gagal mengunduh installer Python. Silakan coba lagi nanti.
        pause
        exit /b
    )

    REM Menjalankan installer Python
    echo Menginstal Python terbaru...
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1

    REM Memeriksa apakah instalasi Python berhasil
    if errorlevel 1 (
        echo Instalasi Python gagal. Pastikan Anda memiliki koneksi internet dan coba lagi.
        pause
        exit /b
    )

    REM Menghapus installer setelah instalasi selesai
    echo Menghapus installer...
    del python_installer.exe
)

echo.
echo Menginstal paket-paket dari requirements.txt...
pip install -r requirements.txt

REM Memeriksa apakah instalasi paket berhasil
if errorlevel 1 (
    echo Instalasi paket dari requirements.txt gagal. Pastikan file tersebut tersedia dan coba lagi.
    pause
    exit /b
)

echo.
echo Menjalankan main.py...
python main.py

REM Memeriksa apakah main.py berhasil dieksekusi
if errorlevel 1 (
    echo Gagal menjalankan main.py. Pastikan file tersebut ada dan tidak ada kesalahan dalam skrip.
    pause
    exit /b
)

echo.
echo Semua perintah telah selesai dieksekusi.
pause
