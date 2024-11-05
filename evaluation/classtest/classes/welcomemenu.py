from classes.menu import menu
from classes.mainmenu import mainmenu


class welcomemenu(menu):
    headline = "Welcome to Track My Habits"
    choices = [
    ]            
    def show(self):
        return
    def execute(self, answer):
        mymenu=mainmenu()
        answer=mymenu.show()
        mymenu.execute(answer)
