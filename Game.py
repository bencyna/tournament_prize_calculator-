from Person import Person
class Game:
    def __init__(self, player1: Person, player2: Person) -> None:
        self.p1 = player1
        self.p2 = player2
        self.p1_odds = None
        self.p2_odds = None
        self.__generateOdds()
        self.winner: Person = None
        self.score = [0, 0]
    
    def __generateOdds(self):
        if self.p1 and self.p2:
            player1_chance = (self.p1.getSkill() / (self.p1.getSkill() + self.p2.getSkill())) * 100
            player2_chance = (self.p2.getSkill() / (self.p1.getSkill() + self.p2.getSkill())) * 100
            self.p1_odds = player1_chance
            self.p2_odds = player2_chance
            
        else:
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
            return self.winner
        else:
            print("No winner yet!") 
            return None

    def setP2(self, player):
        self.p2 = player
        self.__generateOdds()

    def setP1(self, player):
        self.p2 = player
        self.__generateOdds()
    
    def getOdds(self):
        if self.p1_odds != None:
            return self.p1_odds, self.p2_odds
        else:
            print("sorry both players aren't here yet")
        return

 