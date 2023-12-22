import pygame, os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog

# Pré definições.
text_font = ('Impact', 24)
screen_size = '560x220'

class AppGUI:
    def __init__(self, appgui):
        self.appgui = appgui
        self.appgui.title(" ")
        self.appgui.geometry(screen_size)
        self.appgui.resizable(False, False)
        self.appgui.configure(bg = "black")
        self.appgui.attributes("-alpha", 0.95)
        self.estilo = ttk.Style() # Configurar um tema específico para os widgets ttk.
        self.estilo.theme_use("vista") # Nome do tema do ttk.

        self.AppTitle = Label(self.appgui, text = "After Dawn - Music Player", font = text_font, bg = "black", fg = "#7800FF")
        self.AppTitle.grid(row = 1, column = 0, padx = 0, pady = 5)

        self.Playlist_Frame = ttk.Frame(self.appgui)
        self.Playlist_Frame.grid(row = 2, column = 0, padx = 10, pady = 10)

        self.Playlist = tk.Listbox(self.Playlist_Frame, width = 80, height = 6, selectmode = tk.SINGLE)
        self.Playlist.grid(row = 0, column = 0)

        # Volume.
        self.volume_scale = Scale(self.appgui, from_ = 0, to = 100, orient = VERTICAL, command = self.set_volume)
        self.volume_scale.set(50)  # set default volume to 50
        self.volume_scale.grid(row = 2, column = 4)
        
        #self.Playlist = Listbox(self.appgui, width=96, height=6, selectmode = SINGLE)
        #self.Playlist.grid(row = 2, column = 0, padx = 10, pady = 10)

        # Widgets dos controles do player de música.
        self.player_controls()

        # Ativar o Pygame, e a Lista de Músicas.
        self.music_list = []
        pygame.mixer.init()

    def set_volume(self, val):
        volume = int(val) / 100
        pygame.mixer.music.set_volume(volume)

    def pause_song(self):
        pygame.mixer.music.pause()

    def unpause_song(self):
        pygame.mixer.music.unpause()

    def stop_song(self):
        pygame.mixer.music.stop()

    def play_song(self):
        selected_song_index = self.Playlist.curselection()
        if selected_song_index:
            selected_song = self.music_list[selected_song_index[0]]
            pygame.mixer.music.load(selected_song)
            pygame.mixer.music.play()

    def add_song(self):
        song = filedialog.askopenfilename(defaultextension = ".mp3", filetypes=[("MP3 files", "*.mp3")])
        if song:
            self.Playlist.insert(END, os.path.basename(song))
            self.music_list.append(song)

    def player_controls(self):
        # frame do player controls.
        self.controls_frame = Frame(self.appgui)
        self.controls_frame.grid(row = 3, column = 0)

        # Play.
        self.play_button = ttk.Button(self.controls_frame, text = "Tocar", command = self.play_song)
        self.play_button.grid(row = 0, column = 0, padx = 5, pady = 5)

        # Pause.
        self.pause_button = ttk.Button(self.controls_frame, text = "Pausar", command = self.pause_song)
        self.pause_button.grid(row = 0, column = 1, padx = 5, pady = 5)

        # Unpause.
        self.pause_button = ttk.Button(self.controls_frame, text = "Retomar", command = self.unpause_song)
        self.pause_button.grid(row = 0, column = 2, padx = 5, pady = 5)

        # Stop.
        self.stop_button = ttk.Button(self.controls_frame, text = "Parar", command = self.stop_song)
        self.stop_button.grid(row = 0, column = 3, padx = 5, pady = 5)

        # AddMusic.
        self.addmusic_button = ttk.Button(self.controls_frame, text = "Adicionar Música", command = self.add_song)
        self.addmusic_button.grid(row = 0, column = 4, padx = 5, pady = 5)

if __name__ == "__main__":
    appgui = Tk()
    musicplayer = AppGUI(appgui)
    appgui.mainloop()