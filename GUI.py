import tkinter as tk
from tkinter import ttk
from Tournament import Tournament
import math 

class GUI(tk.Frame):
    def __init__(self, parent, tournament: Tournament):
        super().__init__(parent)
        self.parent = parent
        self.tournament = tournament
        self.parent.title("Tournament Generator")
        self.tournament_frame = tk.LabelFrame(self.parent, text="Tournament Details")
        
        self.updateGUI()
        
    def updateGUI(self):
        self.reset_gui()
        # create a frame for the tournament details
        self.tournament_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # display the tournament details
        rounds, players, matches = self.tournament.getTournamentDets()
        tk.Label(self.tournament_frame, text=f"Number of rounds: {rounds}").grid(row=0, column=0, sticky="w")
        tk.Label(self.tournament_frame, text=f"Number of players: {len(players)}").grid(row=1, column=0, sticky="w")
        tk.Label(self.tournament_frame, text=f"Matches: {len(matches)}").grid(row=2, column=0, sticky="w")

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
                else:
                    p1_name = "TBD"
                if game.getP1():
                    p2_name = game.getP2().getName()
                else:
                    p2_name = "TBD"
                
                p1_label = tk.Label(games_frame, text=p1_name)
                p2_label = tk.Label(games_frame, text=f"vs {p2_name}")
                
                p1_label.grid(row=i, column=j*2+1, padx=0, pady=5)
                p2_label.grid(row=i, column=j*2+2, padx=0, pady=5)
                
                # bind click event to labels
                p1_label.bind("<Button-1>", lambda event, p1=p1_name, p2=p2_name: self.on_player_click(event, p1, p2))
                p2_label.bind("<Button-1>", lambda event, p1=p1_name, p2=p2_name: self.on_player_click(event, p1, p2))
                
        
        # create a frame for the odds
        odds_frame = tk.LabelFrame(self.parent, text="Odds")
        odds_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # display the odds
        for i, player in enumerate(players):
            odds_label = tk.Label(odds_frame, text=f"{player.getName()}: {math.floor(player.getOdds()*100)}%")
            odds_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            # except Exception as e:
            #     odds_label = tk.Label(odds_frame, text=f"TBD%")
            #     odds_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    
    def reset_gui(self):
        # Destroy all existing widgets and frames
        for widget in self.parent.winfo_children():
            widget.destroy()

        # Recreate the tournament frame
        self.tournament_frame = tk.LabelFrame(self.parent, text="Tournament Details")

        
    
    def on_player_click(self, event, p1, p2=None):
        if p2 is not None:
            # determine the game that was clicked
            game, round_idx, game_idx = self.tournament.getGame(p1, p2)
            # make the clicked player the winner
            winner = event.widget.cget("text")
            if p1 == winner:
                game.setWinner(game.getP1())
            else:
                game.setWinner(game.getP2())  

            # move the winner to the next round
            self.tournament.addWinnerToNextGame(game.getWinner(), round_idx, game_idx)

            # update the GUI 
            self.updateGUI()
        else:
            print("No player 2, we don't have a valid game yet")