import sqlite3
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
        return

    def createTestData(self):
        self.con.cursor().execute("""
        """)
        return


