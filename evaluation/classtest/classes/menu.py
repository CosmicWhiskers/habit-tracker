from os import system, name
import questionary 

class menu: 
    headline = ""
    choices = []

    def __init__(self):
        return
    
    def clearScreen(self):
        # Clear screen, put this in method somewhere
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def show(self):
        self.clearScreen()
        answer = questionary.select(self.headline, self.choices).ask()
        return answer

    def quitProgram(self):
        exit
