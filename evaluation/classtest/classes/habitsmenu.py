from classes.menu import menu
import classes.mainmenu 
from classes.newhabitmenu import newhabitmenu

class habitsmenu(menu):
    headline = "Manage your habits"
    choices = [
        "New habit",
        "Back to main menu"
    ]            

    def execute(self, answer):
        match answer:
            case "Back to main menu":
                mymenu=classes.mainmenu.mainmenu()
                answer=mymenu.show()
                mymenu.execute(answer)
            case "New habit":
                mymenu=newhabitmenu()
                answer=mymenu.show()
                mymenu.execute(answer)    
