import sqlite3
from classes.db.habit import habit
from datetime import datetime, date, timedelta

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
                                           created_at TIMESTAMP,
                                           lastchange_at TIMESTAMP
                                       )""")

        self.con.cursor().execute("""CREATE TABLE IF NOT EXISTS
                                     habit_history(habit_history_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                     habit_id INTEGER,
                                     check_date DATETIME,
                                     created_at TIMESTAMP,
                                     lastchange_at TIMESTAMP)""")

    
        return

    def createTestData(self):
        myhabit1 = habit(self.con)
        myhabit1.create("Training", "Move body for an hour", 1)

        myhabit1.last_check = date.today() - timedelta(days=50)
        myhabit1.insert()
        myhabit1.addHistory()

        i = 49
        while i > 0:
            newdate = date.today() - timedelta(days=i)
            myhabit1.last_check = newdate
            myhabit1.current_streak += 1
            myhabit1.total_checks += 1
            myhabit1.longest_streak = myhabit1.current_streak
            myhabit1.update()
            myhabit1.addHistory()
            i -= 1

        # Create second habit, with a streak that's incomplete
        myhabit2=habit(self.con)
        myhabit2.last_check = date.today() - timedelta(days=40)
        myhabit2.create("Sleep", "Sleep for 8 hours", 1)
        myhabit2.insert()
        myhabit2.addHistory()

        i = 39
        while i > 0:

            newdate = date.today() - timedelta(days=i)
            myhabit2.last_check = newdate
            myhabit2.total_checks += 1

            if i == 20:
                myhabit2.current_streak = 1
            else:
                myhabit2.current_streak += 1
                if(myhabit2.current_streak > myhabit2.longest_streak):
                    myhabit2.longest_streak = myhabit2.current_streak

            myhabit2.update()
            myhabit2.addHistory()
            i -= 1


        # Habit with no data yet                
        myhabit3 = habit(self.con)      
        myhabit3.create("Hydrate", "Drink 2l of water", 1)
        myhabit3.insert()
        myhabit3.addHistory()


        myhabit4 = habit(self.con)      
        myhabit4.create("Finances", "Check bank statements", 7)

        myhabit4.insert()
        myhabit4.addHistory()

        # Create a weekly habit with some data                   
        myhabit5 = habit(self.con)      
        myhabit5.create("Plants", "Water the plants", 7)
        myhabit5.last_check = date.today() - timedelta(days=40)
        myhabit5.insert()
        myhabit5.addHistory()
        i = 39
        while i > 0:

            newdate = date.today() - timedelta(days=i)
            myhabit5.last_check = newdate

            myhabit5.current_streak += 1
            if(myhabit5.current_streak > myhabit5.longest_streak):
                myhabit5.longest_streak = myhabit5.current_streak

            myhabit5.update()
            myhabit5.addHistory()
            i -= 7

        myhabit6 = habit(self.con)      
        myhabit6.create("Family", "Check on the family", 7)
        myhabit6.insert()
        myhabit6.addHistory()

        return


