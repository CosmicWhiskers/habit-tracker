import sqlite3
#from classes.db.habit import habit
class TestMain:
    con = ""

    def setup_class(self):
        con = sqlite3.connect("testdata.db")
        return

    def teardown_class(self):
        return


    def test_habit_create(self):
        return

