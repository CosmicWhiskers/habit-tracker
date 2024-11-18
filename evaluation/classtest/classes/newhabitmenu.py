from classes.menu import menu
import classes.habitsmenu
import questionary 
from classes.db.habit import habit

class newhabitmenu(menu):
    headline = "Add a new habit"
    choices = [
        "Create habit",
        "Back to habit menu"
    ]            

    def execute(self, answer):
        match answer:
            case "Create habit":
                self.createHabit()
            case "Back to habit menu":
                mymenu=classes.habitsmenu.habitsmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)


    def createHabit(self):
        name = questionary.text("Please enter habit name").ask()
        description = questionary.text("Please enter short habit description").ask()
        type = questionary.select("Please select a type", choices = [questionary.Choice("daily", 1), questionary.Choice("weekly", 7)]).ask()
        

        myHabit = habit(self.con)
        myHabit.create(name, description, type)    
        myHabit.insert()
        print("Habit successfully created")

        questionary.press_any_key_to_continue().ask()
        answer=self.show()
        self.execute(answer)

    
