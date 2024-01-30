from pytube import YouTube

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
    video_url = input("Masukkan URL video YouTube: ")
    download_video(video_url, "./")
