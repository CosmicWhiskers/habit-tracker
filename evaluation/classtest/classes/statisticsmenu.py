from classes.menu import menu
import classes.mainmenu

class statisticsmenu(menu):
    headline = "Your statistics"
    choices = [
        "Show all daily habits",
        "Show all weekly habits",
        "Show longest streak",
        "Back to main menu"

        ]            

    def execute(self, answer):
        match answer:
            case "Back to main menu":
                mymenu=classes.mainmenu.mainmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)
