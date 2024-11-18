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
        self.con.cursor().execute("""CREATE TABLE IF NOT EXISTS 
                                        habit(habit_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                              name TEXT,
                                              description TEXT,
                                              type TEXT,
                                              last_check DATETIME,
                                              total_checks INT,
                                              current_streak INT,
                                              longest_streak INT,
                                              created_at DATETIME,
                                              lastchange_at DATETIME
                                             )""")
        mymenu=mainmenu(self.con)
        answer=mymenu.show()
        mymenu.execute(answer)
        
