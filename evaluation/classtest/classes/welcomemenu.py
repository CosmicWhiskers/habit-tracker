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
        self.con.cursor().execute("CREATE TABLE IF NOT EXISTS habit(habit_id INTEGER PRIMARY KEY, name TEXT, description TEXT, type TEXT, created_at DATETIME, lastchange_at DATETIME)")
        mymenu=mainmenu(self.con)
        answer=mymenu.show()
        mymenu.execute(answer)
        