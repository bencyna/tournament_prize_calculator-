from tkinter import *
from tkinter import ttk
from Tournament import Tournament
import time
class GUI:
    def __init__(self, tournament: Tournament) -> None:
        self.tournament = tournament
        self.matches = []
        self.matchesText = [] # has the tkinter text object
        self.startGui()

    def __buildTournament(self, canvas):
        # add each match to the tournament tree
        y = 5
        x = 5
        for i, round in enumerate(self.matches):
            # different column needed
            column = Widget(width=20, borderwidth=1)
            for match in round:
                # put the matches on the screen
                screen_text1 = "TBA"
                screen_text2 = "TBA"
                p1 = match.getP1()
                p2 = match.getP2()
                if p1:
                    screen_text1 = p1.getName() + " " + str(p1.getRank()) if p1.getRank() else p1.getName()
                if p2:
                    screen_text2 = p2.getName() + " " + str(p2.getRank()) if p2.getRank() else p2.getName()


                text1 = Text(width=10, height=4, font=('Arial', 10), borderwidth=1)
                text2 = Text(width=10, height=4, font=('Arial', 10), borderwidth=1)
                self.matchesText[i].append((text1, text2))
                text1.insert(INSERT, screen_text1)
                text2.insert(INSERT, screen_text2)
                text1.pack(side=TOP, ipadx=5, ipady=5) 
                text2.pack(side=TOP, ipadx=5, ipady=5)


    def startGui(self):
        window = Tk()
        window.config(padx=50, pady=50, width=1000, height=1000, background='white')
        window.title("Tournament")
        canvas = Canvas(width=900, height=600, highlightthickness=0, background="white")
        self.matches = self.tournament.getGames()
        self.matchesText = [[] for round in self.matches]
        self.__buildTournament(canvas)
        window.mainloop()  