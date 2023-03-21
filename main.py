from Person import Person
from Tournament import Tournament
from GUI import GUI
import tkinter as tk

# create people
Will = Person("Will", 75)
Ben = Person("Ben", 60)
Finn = Person("Finn", 60)
Philip = Person("Philip", 30)
max = Person("Max", 75)
Lebron = Person("Lebron", 20)
champ = Person("World Champ", 90)
legend = Person("Legend", 30)
legend2 = Person("Legend2", 30)

# start game
tournament = Tournament([Will, Ben, Finn, Philip, max, Lebron, champ, legend])
# tournament = Tournament([Will, Ben, Finn, Philip])

# give gui the game 
root = tk.Tk()
gui = GUI(root, tournament) 
tournament.showOdds()
 
   