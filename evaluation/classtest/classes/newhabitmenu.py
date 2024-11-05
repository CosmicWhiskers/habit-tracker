from classes.menu import menu
import classes.habitsmenu
import questionary 

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
                mymenu=classes.habitsmenu.habitsmenu()
                answer=mymenu.show()
                mymenu.execute(answer)




    def createHabit(self):
        name = questionary.text("Please enter habit name").ask()
        description = questionary.text("Please enter short habit description").ask()
        type = questionary.select("Please select a type", choices = ["daily", "weekly"]).ask()
        print(name)
        print(description)
        print(type)
        print("Habit successfully created")
        questionary.confirm("Press any key to continue").ask()
        answer=self.show()
        self.execute(answer)