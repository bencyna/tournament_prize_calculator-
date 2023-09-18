from Person import Person
from Tournament import Tournament
from GUI import GUI
import tkinter as tk

# create people
Will = Person("Will", 75)
Ben = Person("Ben", 60)
Finn = Person("Finn", 60)
Philip = Person("Philip", 30)
Jo = Person("Jo", 75)
Declan = Person("Declan", 20)
Callum = Person("Callum", 90)
Vincent = Person("Vincent", 30)
Brad = Person("Brad", 30)

# start game
tournament = Tournament([Will, Ben, Finn, Philip, Jo, Declan, Callum, Vincent])
# tournament = Tournament([Will, Ben, Finn, Philip])
tournament.showOdds()

# give gui the game 
root = tk.Tk()
gui = GUI(root, tournament) 
root.mainloop()
 
