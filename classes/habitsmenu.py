from classes.menu import menu
import classes.mainmenu 
from classes.newhabitmenu import newhabitmenu
from classes.edithabitmenu import edithabitmenu
from classes.deletehabitmenu import deletehabitmenu 

class habitsmenu(menu):
    """ This menu lists all possible actions users can choose to manage their habits.
    """

    headline = "Manage your habits"
    choices = [
        "New habit",
        "Edit an existing habit",
        "Delete a habit",
        "Back to main menu"
    ]            

    def execute(self, answer):
        match answer:
            case "New habit":
                mymenu=newhabitmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)
            case "Edit an existing habit":
                mymenu=edithabitmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)
            case "Delete a habit":
                mymenu=deletehabitmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)   
            case "Back to main menu":
                mymenu=classes.mainmenu.mainmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)