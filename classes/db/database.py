import sqlite3
from classes.db.habit import habit
from datetime import datetime

class database:
    con = ""

    def __init__(self, con):
        self.con = con
        return

    def create(self):
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

        self.con.cursor().execute("""CREATE TABLE IF NOT EXISTS
                                     habit_history(habit_history_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                     habit_id INTEGER,
                                     check_date DATETIME,
                                     created_at DATETIME,
                                     lastchange_at DATETIME)""")

    
        return

    def createTestData(self):
        myhabit1 = habit(self.con)
        myhabit1.create("Training", "Move body for an hour", 1)
        myhabit1.insert()
        myhabit1.addHistory()
        
        myhabit2 = habit(self.con)
        myhabit2.create("Sleep", "Sleep for 8 hours", 1)
        myhabit2.insert()
        myhabit2.addHistory()

        myhabit3 = habit(self.con)      
        myhabit3.create("Hydrate", "Drink 2l of water", 1)
        myhabit3.insert()
        myhabit3.addHistory()

        myhabit4 = habit(self.con)      
        myhabit4.create("Finances", "Check bank statements", 7)
        myhabit4.insert()
        myhabit4.addHistory()

        myhabit5 = habit(self.con)      
        myhabit5.create("Plants", "Water the plants", 7)
        myhabit5.insert()
        myhabit5.addHistory()

        myhabit6 = habit(self.con)      
        myhabit6.create("Family", "Check on the family", 7)
        myhabit6.insert()
        myhabit6.addHistory()

        return


