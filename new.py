from tkinter import Tk, Label, Entry, Button, messagebox
from pytube import YouTube
import os

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_stream.download(output_path)
        messagebox.showinfo("Pengunduhan Selesai", "Video berhasil diunduh!")
    except Exception as e:
        messagebox.showerror("Kesalahan", f"Terjadi kesalahan: {str(e)}")

def clear_entry():
    url_entry.delete(0, 'end')

output_path = "./youtube"

# Create the main window
root = Tk()
root.title("YT Downloader")

# Create and place widgets
Label(root, text="Masukkan URL video YouTube:").pack()
url_entry = Entry(root, width=50)
url_entry.pack()
Button(root, text="Unduh", command=download_video).pack()
Button(root, text="Hapus", command=clear_entry).pack()

root.mainloop()
