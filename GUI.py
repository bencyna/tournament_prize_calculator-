import tkinter as tk

class GUI(tk.Frame):
    def __init__(self, master, tournament):
        super().__init__(master)
        self.tournament = tournament
        self.canvas = tk.Canvas(self, width=800, height=600, bg='white')
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.draw_tree()
    
    def draw_tree(self):
        rounds, players, matches = self.tournament.getTournamentDets()
        game_radius = 25
        game_spacing = 100
        round_spacing = 150
        x = round_spacing
        y = game_spacing + round_spacing

        # Draw nodes
        for i in range(rounds):
            num_games = len(matches[i])
            y += round_spacing
            x_offset = (round_spacing - num_games*game_spacing)/2
            for j in range(num_games):
                game = matches[i][j]
                x_pos = x + x_offset + j*game_spacing
                y_pos = y
                if game.getP1() is not None:
                    self.canvas.create_oval(x_pos-game_radius, y_pos-game_radius,
                                            x_pos+game_radius, y_pos+game_radius, fill='lightblue')
                    self.canvas.create_text(x_pos, y_pos, text=game.getP1().getName())
                if game.getP2() is not None:
                    self.canvas.create_oval(x_pos-game_radius, y_pos+round_spacing-game_radius,
                                            x_pos+game_radius, y_pos+round_spacing+game_radius, fill='lightblue')
                    self.canvas.create_text(x_pos, y_pos+round_spacing, text=game.getP2().getName())

            game_spacing *= 2

        # Draw edges
        game_spacing //= 2
        for i in range(rounds-1):
            num_games = len(matches[i])
            next_num_games = len(matches[i+1])
            x_offset = (round_spacing - num_games*game_spacing)/2
            next_x_offset = (round_spacing - next_num_games*game_spacing)/2
            for j in range(num_games):
                game = matches[i][j]
                x_pos1 = x + x_offset + j*game_spacing
                y_pos1 = y - round_spacing + game_spacing + j*game_spacing
                x_pos2 = x + round_spacing + next_x_offset + j//2*game_spacing*2
                y_pos2 = y + game_spacing + (j//2)*game_spacing*2
                if i == len(matches[i]):
                    self.canvas.create_line(x_pos1, y_pos1+game_radius,
                                            x_pos2, y_pos2-game_radius, width=2, arrow=tk.LAST)
        
        self.pack()
