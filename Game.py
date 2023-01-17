from Person import Person
class Game:
    def __init__(self, player1: Person, player2: Person) -> None:
        self.p1 = player1
        self.p2 = player2
        self.__generateOdds()
        self.winner: Person = None
        self.score = [0, 0]
    
    def __generateOdds(self):
        if self.p1 and self.p2:
            player1_chance = (self.p1.getSkill() / (self.p1.getSkill() + self.p2.getSkill())) * 100
            player2_chance = (self.p2.getSkill() / (self.p1.getSkill() + self.p2.getSkill())) * 100
            return (player1_chance, player2_chance)
        else:
            print("Sorry, 2 players aren't here yet")
            return None

    def getP1(self) -> Person:
        return self.p1

    def getP2(self) -> Person:
        return self.p2

    def setWinner(self, player):
        if player == self.p1 or player == self.p2:
            self.winner = player
            print("winner is" + self.winner.getName())
        else:
            print("Error, player is not in this game")

    def getWinner(self):
        if self.winner:
            return "Winner"
        else:
            print("No winner yet!") 

    def setP2(self, player):
        self.p2 = player

    def setP1(self, player):
        self.p2 = player