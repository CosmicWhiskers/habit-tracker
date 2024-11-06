from classes.menu import menu
import classes.mainmenu 
from classes.newhabitmenu import newhabitmenu
from classes.edithabitmenu import edithabitmenu 

class habitsmenu(menu):
    headline = "Manage your habits"
    choices = [
        "New habit",
        "Edit an existing habit"
        "Choose and delete a habit"
        "Back to main menu"
    ]            

    def execute(self, answer):
        match answer:
            case "New habit":
                mymenu=newhabitmenu()
                answer=mymenu.show()
                mymenu.execute(answer)
            case "Edit an existing habit":
                mymenu=edithabitmenu()
                answer=mymenu.show()
                mymenu.execute(answer)    
            case "Back to main menu":
                mymenu=classes.mainmenu.mainmenu()
                answer=mymenu.show()
                mymenu.execute(answer)