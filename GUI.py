from tkinter import *
from tkinter import ttk
from Tournament import Tournament
import time
class GUI:
    def __init__(self, tournament: Tournament) -> None:
        self.tournament = tournament
        self.matches = []
        self.startGui()

    def __buildTournament(self, canvas):
        # add each match to the tournament tree
        y = 5
        x = 5
        for round in self.matches:
            for match in round:
                # put the matches on the screen
                screen_text = "TBA"
                p1 = match.getP1()
                p2 = match.getP2()
                if p1 and p2:
                    screen_text = f"{p1.getName()} vs {p2.getName()}"

                print(screen_text)
                text = Text(width=10, font=('Arial', 15), borderwidth=1)
                text.insert(INSERT, screen_text)
                text.pack(side=LEFT, ipadx=5, ipady=5)


    def startGui(self):
        window = Tk()
        window.config(padx=50, pady=50, width=1000, height=1000, background='white')
        window.title("Tournament")
        canvas = Canvas(width=900, height=600, highlightthickness=0, background="white")
        self.matches = self.tournament.getGames()
        self.__buildTournament(canvas)
        window.mainloop()