from classes.menu import menu
from classes.habitsmenu import habitsmenu
from classes.checkhabitsmenu import checkhabitsmenu

class mainmenu(menu):
    headline = "Welcome to the main menu."
    choices = [
        "Edit habits",
        "Check off habits",
        "Statistics",
        "Quit"
    ]            

    def execute(self, answer):
        match answer:
            case "Quit":
                self.quitProgram()
            case "Edit habits":
                mymenu=habitsmenu()
                answer=mymenu.show()
                mymenu.execute(answer)
            case "Check off habits":
                mymenu=checkhabitsmenu()
                answer=mymenu.show()
                mymenu.execute(answer)
