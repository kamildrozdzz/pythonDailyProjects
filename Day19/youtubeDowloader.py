import os
import tkinter as tk
from yt_dlp import YoutubeDL

def download():
    try:
        url = link.get()
        ydl_opts = {'outtmpl': 'C:/Users/kamil/Videos/%(title)s.%(ext)s'}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        tk.Label(root, text="Downloaded", font="Arial 15", fg="green").place(x=100, y=120)
    except Exception as e:
        tk.Label(root, text=f"Error: {e}", font="Arial 15", fg="red").place(x=100, y=120)

root = tk.Tk()
root.geometry('500x300')
root.title('Youtube Downloader')

link = tk.StringVar()
tk.Label(root, text="Download Youtube Video", font="Arial 12 bold").pack()
tk.Label(root, text="Paste your link here!!!", font="Arial 12").place(x=150, y=55)
tk.Entry(root, width=70, textvariable=link).place(x=30, y=85)
tk.Button(root, text="Download", font="Arial 14", bg='gray', command=download).place(x=100, y=150)

root.mainloop()
