import sqlite3
import datetime

class habit:
    con = ""
    habit_id = 0
    habit_name = ""
    habit_description = ""
    habit_type = 0

    
    def __init__(self, con):
        self.con = con

    def create(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type

    def insert(self):
        sql = "INSERT INTO habit (name, description, type, created_at, lastchange_at) VALUES (?,?,?,?,?)"

        data_tuples = (self.name, self.description, self.type, datetime.datetime.now(), datetime.datetime.now())
        self.con.cursor().execute(sql, data_tuples)
        self.con.commit()
