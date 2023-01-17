from Person import Person
import math
class Tournament:
    def __init__(self, people: list[Person]) -> None:
        if len(people) < 4:
            print("Requires a minimum of 4 people")
            return
        self.players_len = len(people)
        self.players = people.sort(key=lambda x:x.getSkill())
        self.rounds = 0
        self.matches = []
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
          self.matches = [[] for _ in range(rounds-1)]
          # create the games with each seeded player on a corner

        
    def showOdds(self) -> None:
        for player in self.players:
            print(f"{player.getName()} has a {round(player.getOdds()*100, 2)}% chance of winning")

    def addPerson(self, person) -> None:
        self.players.append(person)
        self.players_len += 1 
    
    def getTournamentDets(self):
        return self.rounds, self.players, self.matches

    