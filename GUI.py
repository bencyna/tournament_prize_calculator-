import tkinter as tk
from Tournament import Tournament
import time
class GUI:
    def __init__(self, tournament: Tournament) -> None:
        self.tournament = tournament
        self.matches = []
        self.matchesText = [] # has the tkinter text object
        self.__buildTournament()

    def __buildTournament(self):
        # add each match to the tournament tree
        y = 5
        x = 5
        for i, round in enumerate(self.matches):
            # different column needed
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

        self.create_widgets()
    def create_widgets(self):
        # Create the tournament tree using labels
        labels = []
        num_matches = len(self.matches)
        for i in range(num_matches):
            labels.append(tk.Label(self.root, text=f"{self.matches[i][0]} vs. {self.matches[i][1]}"))
            labels[i].grid(row=i, column=0)
        print(labels)
        # Create labels for the current round and player names
        round_label = tk.Label(self.root, text=f"Current Round: {self.current_round}")
        round_label.grid(row=num_matches, column=0)

        player_label = tk.Label(self.root, text="Players:")
        player_label.grid(row=0, column=1)
        for i in range(self.num_players):
            player_name = tk.Label(self.root, text=f"{self.player_names[i]} ({self.player_skills[i]})")
            player_name.grid(row=i+1, column=1)

        self.root.mainloop()  