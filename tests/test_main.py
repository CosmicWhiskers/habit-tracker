import sqlite3
import os
from classes.db.habit import habit
from classes.db.database import database

class TestMain:
    con = ""

    def setup_class(self):
        self.con = sqlite3.connect("testdata.db")

        mydb = database(self.con)

        mydb.create()
        mydb.createTestData()
        return

    def teardown_class(self):
        os.remove("testdata.db")
        return

    def test_habit_create(self):
        return

