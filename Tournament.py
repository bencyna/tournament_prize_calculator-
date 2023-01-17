from Person import Person
from Game import Game
import math
import random
class Tournament:
    def __init__(self, people: list[Person], group: bool = False) -> None:
        if len(people) < 4:
            print("Requires a minimum of 4 people")
            return
        self.players_len = len(people)
        self.players = sorted(people, key=lambda x:x.getSkill())
        self.rounds = 0
        self.currentRound = 0
        self.matches = []
        self.seed = set() 
        print(self.players[:len(self.players)//2])
        if not group:
            for player in self.players[:len(self.players)//2]:
                self.seed.add(player)
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
        self.matches = [[] for _ in range(self.rounds-1)]
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

        #games created
        #

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