from classes.menu import menu
import classes.habitsmenu

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
        print ("Simone ist")
        exit
