import os
import tkinter as tk
from tkinter import filedialog
import pygame


class MusicPlayer(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Shubham Music Player")
        self.geometry("400x150")
        self.current_track = ""
        self.playing = False

        pygame.init()

        self.label = tk.Label(self, text="Select a song to play.")
        self.label.pack()

        self.play_button = tk.Button(self, text="Play", command=self.play_pause)
        self.play_button.pack()

        self.select_button = tk.Button(self, text="Select Song", command=self.select_song)
        self.select_button.pack()

        self.volume_scale = tk.Scale(self, from_=0, to=100, orient="horizontal", command=self.adjust_volume)
        self.volume_scale.set(50)
        self.volume_scale.pack()

    def select_song(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3",
                                               filetypes=[("MP3 Files", ".mp3"), ("All Files", ".*")])
        if file_path:
            self.current_track = file_path
            self.label.config(text=f"Now playing: {os.path.basename(file_path)}")

    def play_pause(self):
        if self.current_track:
            if not self.playing:
                pygame.mixer.music.load(self.current_track)
                pygame.mixer.music.play()
                self.playing = True
                self.play_button.config(text="Pause")
            else:
                pygame.mixer.music.pause()
                self.playing = False
                self.play_button.config(text="Play")

    def adjust_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume) / 100)

if _name_ == "_main_":
    app = MusicPlayer()
    app.mainloop()