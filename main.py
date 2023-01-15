from Person import Person
from Tournament import Tournament
from Game import Game
from GUI import GUI

# create people
Will = Person("Will", 85)
Ben = Person("Ben", 60)
Finn = Person("Finnl", 60)
Philip = Person("Philip", 30)

# start game
tournament = Tournament([Will, Ben, Finn, Philip])
#give gui the game
gui = GUI(tournament) 
# tournament.showOdds() 