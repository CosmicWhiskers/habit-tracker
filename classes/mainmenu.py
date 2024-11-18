from classes.menu import menu
from classes.habitsmenu import habitsmenu
from classes.checkhabitsmenu import checkhabitsmenu
from classes.statisticsmenu import statisticsmenu

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
            case "Edit habits":
                mymenu=habitsmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)
            case "Check off habits":
                mymenu=checkhabitsmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)
            case "Statistics":
                mymenu=statisticsmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)
            case "Quit":
                self.quitProgram()

