from Person import Person
from Game import Game

Will = Person("Will", 85)
Ben = Person("Ben", 60)
Finn = Person("Finnl", 60)
Philip = Person("Philip", 30)
game = Game([Will, Ben, Finn, Philip])
game.showOdds()