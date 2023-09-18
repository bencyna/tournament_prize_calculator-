from Person import Person
from Game import Game
import math
import random
from collections import defaultdict

class Tournament:
    def __init__(self, people: list[Person], entry_fee = 10, group: bool = False) -> None:
        if len(people) < 4:
            print("Requires a minimum of 4 people")
            return
        self.players_len = len(people)
        self.players = sorted(people, reverse=True, key=lambda x:x.getSkill())
        self.rounds = 0
        self.currentRound = 0
        self.matches = []
        self.seed = set() 
        self.player_wins = {}
        self.entry_fee = entry_fee

        # if no group stage, generate the seeds here
        if not group:
            for i, player in enumerate(self.players[:len(self.players)//2]):
                self.seed.add(player)
                player.setRank(i+1)
        self.__generateOdds()
        self.__generateGameTree()

    def __generateOdds(self) -> None:
        skill_sum = 0
        for person in self.players:
            skill_sum += person.getSkill()
        
        for player in self.players:
            player.setOdds(player.getSkill()/skill_sum)

    def __generateGameTree(self):
        self.rounds = math.ceil(math.log2(self.players_len))
        #set matches tournament to a matrix
        self.matches = [[] for _ in range(self.rounds)]
        # create the games with each seeded player on a cornerm should be random for non group stages
        games_to_add = math.ceil(len(self.players)/2)
        for player in self.seed:
            game = Game(player, None)
            self.matches[0].append(game)
        
        matchIndex = 0
        for player in sorted(self.players ,key=lambda _: random.random()):
            if player not in self.seed:
                self.matches[0][matchIndex].setP2(player)
                matchIndex += 1

        # this should set up all the matches to come with no one in them yet
        # first round is set up
        matchesLeft = matchIndex//2
        for i in range(1, self.rounds):
            for _ in range(matchesLeft):
                game = Game(None, None)
                self.matches[i].append(game)
            matchesLeft //= 2


    def showOdds(self) -> None:
        for player in self.players:
            print(f"{player.getName()} has a {round(player.getOdds()*100, 2)}% chance of winning")

    def addPerson(self, person) -> None:
        self.players.append(person)
        self.players_len += 1 
    
    def getTournamentDets(self):
        return self.rounds, self.players, self.matches

    def getGames(self):
        return self.matches
    
    def getGame(self, p1, p2):
        for round_idx, round in enumerate(self.matches):
            for game_idx, game in enumerate(round):
                if p1 == game.getP1().getName() and p2 == game.getP2().getName():
                    return game, round_idx, game_idx
            
        return None
    
       
    def getTournamentDets(self):
        return self.rounds, self.players, self.matches   
    

    def addWinnerToNextGame(self, winner, round_idx, game_idx):
        if round_idx == self.rounds-1:
            # we have an ultimate winner
            self.setTournamentWinner(winner)
        else:
            new_round = round_idx + 1
            new_game_idx = game_idx//2
            # set players in game by index
            if game_idx % 2 == 0:
                self.matches[new_round][new_game_idx].setP1(winner)
            else:
                self.matches[new_round][new_game_idx].setP2(winner)
            
    def setTournamentWinner(self, winner):
        print(winner.getName() + " wins!")
        self.generatePrizeMoney(winner)
        
    def generatePrizeMoney(self, winner):
        # loop through all the matches and add each win to player wins
        for i, round in enumerate(self.matches):
            for j, game in enumerate(round):
                winner = game.getWinner()
                winner.wonGame()

        # 
        money = {}
        total = len(self.players) * self.entry_fee
        for player in self.players:
            prize_money = self.calculate_prize(player, self.entry_fee)
            money[player.getName()] = prize_money
            total -= prize_money
            
        print(money, total)
        
        money_back = total/len(self.players)
        
        for name, money_so in money.items():
            money[name] += money_back
            
        self.reset_wins()
            
    def calculate_prize(self, person: Person, entry_fee):
        # Define a factor for progression. Higher rounds should have higher factors.
        win_factors = {0: .5, 1: 1, 2: 1.5, 3: 2, 4:2.5}  # Adjust as needed
        
        # Calculate prize based on skill level, winning probability, and round
        progression_factor = person.getWins()
        chance_factor = 1 - person.getOdds() 

        prize = (((chance_factor) * win_factors[progression_factor] * entry_fee)) 
        
        return prize

    def reset_wins(self):
        for player in self.players:
            player.resetWins()