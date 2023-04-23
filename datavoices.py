import sqlite3
db = sqlite3.connect('database.db')
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users (
questions TEXT,
answers TEXT)
""")
db.commit()

DiffData = sqlite3.connect('database.db')
DiffCur = DiffData.cursor()
DiffCur.execute("""CREATE TABLE IF NOT EXISTS diffurs (
questions TEXT,
answers TEXT)
""")
DiffData.commit()

connect = sqlite3.connect('database.db', check_same_thread=False)
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS marks (
id key,
score int)
""")
connect.commit()