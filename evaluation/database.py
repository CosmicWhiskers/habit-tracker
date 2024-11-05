import sqlite3

con = sqlite3.connect("habbit-tracker.db")

cur = con.cursor()

# Create
cur.execute("CREATE TABLE IF NOT EXISTS habbit(habbit_id, name, description)")

# Insert
cur.execute("INSERT INTO habbit (habbit_id, name, description) VALUES (1, 'Test', 'Test description')")
# Select

result = cur.execute("SELECT * FROM habbit")

# Delete
result = cur.execute("DELETE FROM habbit where habbit_id = 1")
