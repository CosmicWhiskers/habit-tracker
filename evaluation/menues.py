from os import system, name
from time import sleep
import questionary 


# Clear screen, put this in method somewhere
if name == 'nt':
    _ = system('cls')
# for mac and linux(here, os.name is 'posix')
else:
    _ = system('clear')


# Simple menu
answer = questionary.select("Welcome to the main menu.", choices=[
    "Edit habits",
    "Check off habits",
    "Statistics",
    "Quit"]).ask()


if(answer == "Quit"):
    exit
else: 
    print(answer)
