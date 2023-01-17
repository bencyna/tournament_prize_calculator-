from tkinter import *
from tkinter import ttk
from Tournament import Tournament
import time
class GUI:
    def __init__(self, tournament: Tournament) -> None:
        self.tournament = tournament
        self.matches = []
        self.startGui()

    def startGui(self):
        window = Tk()
        window.config(padx=50, pady=50, width=900, height=700, background='white')
        window.title("Tournament")
        self.matches = self.tournament.getGames()
        window.mainloop()