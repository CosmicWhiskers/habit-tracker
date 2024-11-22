from classes.menu import menu
from classes.mainmenu import mainmenu
from classes.db.database import database
import os
import sqlite3
import questionary

class welcomemenu(menu):
    """ Starter menu. Initializes application. 
    """
    headline = "Welcome to Track My Habits"
    choices = [
    ]            

    def __init__(self):
        return

    def show(self):
        return
    def execute(self, answer):
        # this method either connects to or creates a database. 
        # If no database exists the new database, initial data will be added.
        if os.path.isfile("habit-tracker.db"):
            self.con = sqlite3.connect("habit-tracker.db")
        else:
            self.con = sqlite3.connect("habit-tracker.db")

            questionary.print("Creating new database if not already existing!")
            mydb = database(self.con)
            mydb.create()

            questionary.print("Adding initial data...")
            mydb.createTestData()

            questionary.print("Completed initialization!")
            questionary.press_any_key_to_continue().ask()

        mymenu=mainmenu(self.con)
        answer=mymenu.show()
        mymenu.execute(answer)

