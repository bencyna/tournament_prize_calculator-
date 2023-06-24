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
                    p1_name = game.getP1().getName()
                    p2_name = game.getP2().getName()
                    game_label = tk.Label(games_frame, text=f"{game.getP1().getName()} vs {game.getP2().getName()}")
                    game_label.grid(row=i, column=j+1, padx=10, pady=5)
                     # bind click event to label
                    game_label.bind("<Button-1>", lambda event, p1=p1_name, p2=p2_name: self.on_player_click(event, p1, p2))
                else:
                    game_label = tk.Label(games_frame, text=f"TBD")
                    game_label.grid(row=i, column=j+1, padx=10, pady=5)
                    
        # create a frame for the odds
        odds_frame = tk.LabelFrame(self.parent, text="Odds")
        odds_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # display the odds
        for i, player in enumerate(players):
            try:
                odds_label = tk.Label(odds_frame, text=f"{player.getName()}: {round(player.getOdds()*100, 2)}%")
                odds_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            except (Exception):
                odds_label = tk.Label(odds_frame, text=f"TBD%")
                odds_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
                
    def on_player_click(self, event, p1, p2=None):
        if p2 is not None:
            print("eror here?")
            
            # determine the game that was clicked
            game = self.tournament.getGame(p1, p2)
            print("eror here?")


            # make the clicked player the winner
            if event.widget == event.widget.master.children["!label"]:
                game.setWinner(game.getP1())
            else:
                game.setWinner(game.getP2())

            # move the winner to the next round
            if game.getNextGame():
                next_game = game.getNextGame()
                if next_game.getP1() is None:
                    next_game.setP1(game.getWinner())
                elif next_game.getP2() is None:
                    next_game.setP2(game.getWinner())

            # update the GUI 
            self.update_gui()