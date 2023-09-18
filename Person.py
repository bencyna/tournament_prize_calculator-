class Person:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.percOdds = 0 
        self.wins = 0
        self.rank = 0

    def increment_skill(self):
        self.skill += 5 if self.skill < 100 else 0

    def decrement_skill(self):
        self.skill -= 5 if self.skill > 5 else 0

    def getSkill(self) -> int:
        return self.skill

    def getName(self) -> str:   
        return self.name

    def getOdds(self) -> int:
        return self.percOdds

    def setOdds(self, odds) -> None:
        self.percOdds = odds
    
    def setRank(self, seed):
        self.rank = seed

    def getRank(self):
        return self.rank
    
    def wonGame(self):
        self.wins += 1
        
    def getWins(self):
        return self.wins
    
    def resetWins(self):
        self.wins = 0
        