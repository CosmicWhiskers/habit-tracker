from classes.menu import menu
from classes.mainmenu import mainmenu
from classes.db.database import database
import sqlite3
import questionary

class welcomemenu(menu):
    headline = "Welcome to Track My Habits"
    choices = [
    ]            
    def show(self):
        return
    def execute(self, answer):
        questionary.print("Creating new database if not already existing!")
        mydb = database(self.con)

        mydb.create()
        questionary.press_any_key_to_continue().ask()
        mymenu=mainmenu(self.con)
        answer=mymenu.show()
        mymenu.execute(answer)
        
