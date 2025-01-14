import vlc
import os
import tkinter as tk

import tkinter as tk
from tkinter import ttk
import vlc

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import imageio

# fake = 'livestream_server/livestream_server/out.mp4'
store = ''

class VideoPlayer(tk.Tk):
    def __init__(self, video_path):
        super().__init__()
        self.title("Video Player")
        self.geometry("1200x800")

        # Tkinter frame to embed the video
        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(fill=tk.BOTH, expand=1)

        self.video_path = video_path
        self.video = imageio.get_reader(video_path)
        self.play_video()

    def play_video(self):
        try:
            for frame in self.video.iter_data():
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                self.update()
                self.after(30)  # Adjust the delay to match the video frame rate
        except RuntimeError:
            pass

if __name__ == "__main__":
    app = VideoPlayer(store)
    print("THIS PLAYED :-)")
    app.mainloop()