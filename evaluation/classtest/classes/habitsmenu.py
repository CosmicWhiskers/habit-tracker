from classes.menu import menu
import classes.mainmenu 

class habitsmenu(menu):
    headline = "Manage your habits"
    choices = [
        "New habits",
        "Edit habits",
        "Delete habit",
        "Back to main menu"
    ]            

    def execute(self, answer):
        match answer:
            case "Back to main menu":
                mymenu=classes.mainmenu.mainmenu()
                answer=mymenu.show()
                mymenu.execute(answer)
                
