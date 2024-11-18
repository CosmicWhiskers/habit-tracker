import sqlite3
import os
import datetime
from classes.db.habit import habit
from classes.db.database import database

class TestMain:
    con = ""
    
    def adapt_date_iso(val):
        """Adapt datetime.date to ISO 8601 date."""
        return val.isoformat()

    def adapt_datetime_iso(val):
        """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
        return val.isoformat()

    def adapt_datetime_epoch(val):
        """Adapt datetime.datetime to Unix timestamp."""
        return int(val.timestamp())
    def convert_date(val):
        """Convert ISO 8601 date to datetime.date object."""
        return datetime.date.fromisoformat(val)
        
    def convert_datetime(val):
        """Convert ISO 8601 datetime to datetime.datetime object."""
        return datetime.datetime.fromisoformat(val)
        
    def convert_timestamp(val):
        """Convert Unix epoch timestamp to datetime.datetime object."""
        return datetime.datetime.fromtimestamp(val)


    def setup_class(self):
        sqlite3.register_adapter(datetime.date, self.adapt_date_iso)
        sqlite3.register_adapter(datetime.datetime, self.adapt_datetime_iso)
        sqlite3.register_adapter(datetime.datetime, self.adapt_datetime_epoch)

        sqlite3.register_converter("date", self.convert_date)
        sqlite3.register_converter("datetime", self.convert_datetime)
        sqlite3.register_converter("timestamp", self.convert_timestamp)

        self.con = sqlite3.connect("testdata.db")

        mydb = database(self.con)

        mydb.create()
        mydb.createTestData()
        return

    def teardown_class(self):
        os.remove("testdata.db")
        return

    def test_habit_create(self):
        myhabit=habit(self.con)
        myhabit.create("Test1", "TestDesc", 1)
        myhabit.insert()        

        assert myhabit.name == "Test1"
        assert myhabit.description == "TestDesc"
        assert myhabit.htype == 1
        assert myhabit.hid == 7

        myhabit2=habit(self.con)
        myhabit2.create("Test2", "TestDesc", 1)
        myhabit2.insert()

        assert myhabit2.hid == 8

        myhabit2.name = "Test3"
        myhabit2.update()

        assert myhabit2.name == "Test3"

        myhabit3=habit(self.con)
        myhabit3.getByHabitId(8)

        assert myhabit3.name == "Test3"
        assert myhabit3.description == "TestDesc"
        assert myhabit3.hid == 8

        return

