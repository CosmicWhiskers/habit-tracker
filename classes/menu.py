from os import system, name
import questionary 

class menu: 
    headline = ""
    choices = []
    con=""
    def __init__(self,con):
        self.con=con
        return
    
    def clearScreen(self):
        return
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

    def getAllHabitsAsChoices(self): 
        result = self.con.cursor().execute("SELECT * FROM habit")   

        choices = []
        for x in result:
            print(x)
            state = "Daily" if int(x[3]) == 1 else "Weekly"
            choices.append(questionary.Choice(x[1] + ": " + x[2] + " -> " + state, x[0]))

        choices.append(questionary.Choice("Back to previous menu", -1))
        
        return choices

    def quitProgram(self):
        exit
