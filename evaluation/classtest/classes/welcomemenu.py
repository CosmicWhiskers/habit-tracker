from classes.menu import menu
from classes.mainmenu import mainmenu
import sqlite3

class welcomemenu(menu):
    headline = "Welcome to Track My Habits"
    choices = [
    ]            
    def show(self):
        return
    def execute(self, answer):
        mymenu=mainmenu(self.con)
        answer=mymenu.show()
        mymenu.execute(answer)
        