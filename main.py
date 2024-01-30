from pytube import YouTube
from colorama import Fore, Style
import pyfiglet
import os
import requests
from tqdm import tqdm

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
        file_size = video_stream.filesize
        response = requests.get(video_stream.url, stream=True)
        with open(os.path.join(output_path, 'video.mp4'), 'wb') as f:
            with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, desc="Progress") as pbar:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
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
