from classes.welcomemenu import welcomemenu
import sqlite3
con = sqlite3.connect("habit-tracker.db")

mymenu = welcomemenu(con)

answer = mymenu.show()

mymenu.execute(answer)
