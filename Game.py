class Game:
    def __init__(self, people):
        self.players_len = len(people)
        self.players = people
        self.__generateOdds()

    def __generateOdds(self):
        skill_sum = 0
        for person in self.players:
            skill_sum += person.getSkill()
        averageSkill = skill_sum // self.players_len
    

    def addPerson(self, person):
        self.players.append(person)
        self.players_len += 1