from classes.menu import menu
import classes.mainmenu

class statisticsmenu(menu):
    headline = "Your statistics"
    choices = [
        "Back to main menu"
    ]            

    def execute(self, answer):
        match answer:
            case "Back to main menu":
                mymenu=classes.mainmenu.mainmenu()
                answer=mymenu.show()
                mymenu.execute(answer)
