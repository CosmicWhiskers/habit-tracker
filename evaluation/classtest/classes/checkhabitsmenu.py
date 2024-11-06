from classes.menu import menu
import classes.mainmenu

class checkhabitsmenu(menu):
    headline = "Check off your habits"
    choices = [
        "Back to main menu"
    ]            

    def execute(self, answer):
        match answer:
            case "Back to main menu":
                mymenu=classes.mainmenu.mainmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)
