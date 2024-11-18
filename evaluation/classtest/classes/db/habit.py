import sqlite3
import datetime
from datetime import date, datetime

class habit:
    con = ""
    id = 0
    name = ""
    description = ""
    htype = 0
    last_check = ""
    total_checks = 0
    current_streak = 0
    longest_streak = 0
    created_at = 0
    lastchange_at = 0

    def __init__(self, con):
        self.con = con


    def getByHabitId(self, habbit_id):
        result = self.con.cursor().execute("SELECT * FROM habit where habit_id = " + str(habbit_id)).fetchone()
        print(result)
        self.id = result[0]
        self.name = result[1]
        self.description = result[2]
        self.htype = result[3]
        self.last_check = result[4]
        self.total_checks = result[5]
        self.current_streak = result[6]
        self.longest_streak = result[7]
        self.created_at = result[8]
        self.lastchange_at = result[9]

    def create(self, name, description, type):
        self.name = name
        self.description = description
        self.htype = type
        self.last_check = date.today()
        self.total_checks = 1
        self.current_streak = 1
        self.longest_streak = 1
        created_at = datetime.now()
        lastchange_at = datetime.now()

    def insert(self):
        sql = "INSERT INTO habit (name, description, type, last_check, total_checks, current_streak, longest_streak, created_at, lastchange_at) VALUES (?,?,?,?,?,?,?,?,?)"

        data_tuples = (self.name, self.description, self.htype, self.last_check, self.total_checks, self.current_streak, self.longest_streak, self.created_at, self.lastchange_at)
        self.con.cursor().execute(sql, data_tuples)
        self.con.commit()

        self.id = self.con.cursor().lastrowid

    def update(self):
        sql = "UPDATE habit set name = ?, description = ?, type = ?, last_check = ?, total_checks = ?, current_streak = ?, longest_streak = ?, created_at = ?, lastchange_at = ?"

        self.lastchange_at = datetime.now()
        data_tuples = (self.name, self.description, self.htype, self.last_check, self.total_checks, self.current_streak, self.longest_streak, self.created_at, self.lastchange_at)
        self.con.cursor().execute(sql, data_tuples)
        self.con.commit()

    def delete(self):
        sql = "DELETE from habit where habit_id = ?"
        data_tuples = (self.id,)
        self.con.cursor().execute(sql, data_tuples)
        self.con.commit()

