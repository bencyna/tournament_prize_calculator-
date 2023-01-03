class Person:
 def __init__(self, name, skill):
    self.name = name
    self.skill = skill

    def increment_skill(self):
        self.skill += 5 if self.skill < 100 else 0

    def decrement_skill(self):
        self.skill -= 5 if self.skill > 5 else 0

    def getSkill(self) -> int:
        return self.skill
    
    def getName(self) -> str:   
        return self.name

    