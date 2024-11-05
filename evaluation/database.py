import sqlite3

con = sqlite3.connect("habit-tracker.db")

cur = con.cursor()

# Create
cur.execute("CREATE TABLE IF NOT EXISTS habit(habit_id, name, description)")

# Insert
cur.execute("INSERT INTO habit (habit_id, name, description) VALUES (1, 'Test', 'Test description')")
# Select

result = cur.execute("SELECT * FROM habit")

# Delete
result = cur.execute("DELETE FROM habit where habit_id = 1")
