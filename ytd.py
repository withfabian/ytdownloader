from pytube import YouTube
from colorama import Fore, Style
import pyfiglet
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    banner = pyfiglet.figlet_format("YT Downloader", font="slant")
    rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    rainbow_banner = ''
    for i, char in enumerate(banner):
        rainbow_banner += rainbow_colors[i % len(rainbow_colors)] + char
    print(rainbow_banner)
    print()

def show_menu():
    print("╔═════════════════════════════════════════╗")
    print("║               \033[1;33m🌟  MENU  🌟\033[0m              ║")
    print("╠═════════════════════════════════════════╣")
    print("║  \033[1;36m1\033[0m. Unduh video dari YouTube            ║")
    print("║  \033[1;36m2\033[0m. Keluar                              ║")
    print("╚═════════════════════════════════════════╝")
    print()

def download_video(url, output_path='.'):
    try:
        show_banner()
        print("Memulai pengunduhan...\n")
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_stream.download(output_path)
        print("\nPengunduhan selesai!")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    while True:
        show_banner()
        show_menu()
        choice = input("Pilih menu: ")

        if choice == '1':
            video_url = input("Masukkan URL video YouTube: ")
            download_video(video_url, "./youtube")
            input("\nTekan Enter untuk kembali ke menu...")
        elif choice == '2':
            print("\nTerima kasih telah menggunakan program ini.")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")
            input("\nTekan Enter untuk kembali ke menu...")
