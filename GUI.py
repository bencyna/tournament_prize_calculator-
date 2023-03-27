import tkinter as tk
from tkinter import ttk
from Tournament import Tournament

class GUI(tk.Frame):
    def __init__(self, parent, tournament: Tournament):
        super().__init__(parent)
        self.parent = parent
        self.tournament = tournament
        self.parent.title("Tournament Generator")

        # create a frame for the tournament details
        tournament_frame = tk.LabelFrame(self.parent, text="Tournament Details")
        tournament_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # display the tournament details
        rounds, players, matches = self.tournament.getTournamentDets()
        tk.Label(tournament_frame, text=f"Number of rounds: {rounds}").grid(row=0, column=0, sticky="w")
        tk.Label(tournament_frame, text=f"Number of players: {len(players)}").grid(row=1, column=0, sticky="w")
        tk.Label(tournament_frame, text=f"Matches: {len(matches)}").grid(row=2, column=0, sticky="w")

        # create a frame for the games
        games_frame = tk.LabelFrame(self.parent, text="Games")
        games_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # display the games
        games = self.tournament.getGames()
        for i, round in enumerate(games):
            round_label = tk.Label(games_frame, text=f"Round {i+1}")
            round_label.grid(row=i, column=0, sticky="w")
            for j, game in enumerate(round):
                if game.getP1():
                    game_label = tk.Label(games_frame, text=f"{game.getP1().getName()} vs {game.getP2().getName()}")
                    game_label.grid(row=i, column=j+1, padx=10, pady=5)
                else:
                    game_label = tk.Label(games_frame, text=f"TBD")
                    game_label.grid(row=i, column=j+1, padx=10, pady=5)
                    
        # create a frame for the odds
        odds_frame = tk.LabelFrame(self.parent, text="Odds")
        odds_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # display the odds
        # for i, player in enumerate(players):
        #     if player:
        #         odds_label = tk.Label(odds_frame, text=f"{player.getName()}: {round(player.getOdds()*100, 2)}%")
        #         odds_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        #     else:
        #         odds_label = tk.Label(odds_frame, text=f"TBD%")
        #         odds_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
                
