from Person import Person
class Game:
    def __init__(self, people: list[Person]) -> None:
        self.players_len = len(people)
        self.players = people
        self.__generateOdds()

    def __generateOdds(self) -> None:
        skill_sum = 0
        for person in self.players:
            skill_sum += person.getSkill()
        
        for player in self.players:
            player.setOdds(player.getSkill()/skill_sum)

        
    def showOdds(self) -> None:
        for player in self.players:
            print(f"{player.getName()} has a {round(player.getOdds()*100, 2)}% chance of winning")

    def addPerson(self, person) -> None:
        self.players.append(person)
        self.players_len += 1