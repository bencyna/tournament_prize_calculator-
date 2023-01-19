from tkinter import *
from tkinter import ttk
from Tournament import Tournament
import time
class GUI:
    def __init__(self, tournament: Tournament) -> None:
        self.tournament = tournament
        self.matches = []
        self.startGui()

    def __buildTournament(self):
        # add each match to the tournament tree
        y = 50
        x = 50
        for round in self.matches:
            for match in round:
                print(match)

    def startGui(self):
        window = Tk()
        window.config(padx=50, pady=50, width=900, height=700, background='white')
        window.title("Tournament")
        frame = Frame(borderwidth=5, relief=SUNKEN)
        frame.pack()
        text = Text(width=50, font=('Times New Roman', 15, 'italic'), borderwidth=0)
        text.insert(INSERT, "Start typing...")
        text.pack(side=TOP, ipadx=30, ipady=10)
        canvas = Canvas(width=900, height=600, highlightthickness=0, background="white")
        canvas.pack()
        self.matches = self.tournament.getGames()
        self.__buildTournament()
        window.mainloop()