import sqlite3

DB_FILE = "data/database.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

"""Create the user, saves, and achievements database if not already created"""

command = "CREATE TABLE IF NOT EXISTS accts(userid INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, password TEXT)"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS saves(user TEXT, times TEXT, lat TEXT, long TEXT, address TEXT, summary TEXT, high TEXT, low TEXT, curr TEXT, attraction TEXT)"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS achievements(user TEXT, accomplishment TEXT)"
c.execute(command)

db.commit()
db.close()
