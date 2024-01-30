from pytube import YouTube
from colorama import Fore, Back, Style
import pyfiglet

def show_banner():
    banner = pyfiglet.figlet_format("YT Downloader")
    rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    rainbow_banner = ''
    for i, char in enumerate(banner):
        rainbow_banner += rainbow_colors[i % len(rainbow_colors)] + char
    print(rainbow_banner)

def show_menu():
    print("╔═════════════════════════════════════════╗")
    print("║               \033[1;33m🌟  MENU  🌟\033[0m              ║")
    print("╠═════════════════════════════════════════╣")
    print("║  \033[1;36m1\033[0m. Unduh video dari YouTube            ║")
    print("║  \033[1;36m2\033[0m. Keluar                              ║")
    print("╚═════════════════════════════════════════╝")

def download_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        
        # Mendapatkan stream video dengan kualitas tertinggi yang mencakup baik video maupun audio
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Mendownload video ke output_path
        video_stream.download(output_path)

        print("Unduhan selesai!")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    show_banner()
    while True:
        show_menu()
        choice = input("Pilih menu: ")

        if choice == '1':
            video_url = input("Masukkan URL video YouTube: ")
            download_video(video_url, "./")
        elif choice == '2':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")
