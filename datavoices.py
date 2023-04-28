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

sol = sqlite3.connect('database.db')
curp = sol.cursor()
curp.execute("""CREATE TABLE IF NOT EXISTS solution (
integral TEXT,
diffurs TEXT)
""")
sol.commit()
def IntegralQuestion(Num1):
    Num1 = int(Num1)
    db1 = sqlite3.connect('database.db')
    cur2 = db1.cursor()
    cur2.execute('SELECT questions from users')
    rows = cur2.fetchall()[Num1][0]
    cur2.close()
    return rows


def IntegralAnswer(Num2):
    Num2 = int(Num2)
    db2 = sqlite3.connect('database.db')
    cur3 = db2.cursor()
    cur3.execute("SELECT answers FROM users")
    rows = cur3.fetchall()[Num2][0]
    cur3.close()
    return rows


def DiffursQuestion(Num1):
    Num1 = int(Num1)
    db1 = sqlite3.connect('database.db')
    cur2 = db1.cursor()
    cur2.execute('SELECT questions from diffurs')
    rows = cur2.fetchall()[Num1][0]
    cur2.close()
    return rows


def DiffursAnswer(Num2):
    Num2 = int(Num2)
    db2 = sqlite3.connect('database.db')
    cur3 = db2.cursor()
    cur3.execute('SELECT answers from diffurs')
    rows = cur3.fetchall()[Num2][0]
    cur3.close()
    return rows

def ChooseIntSolution(Num1):
    Num1 = int(Num1)
    db1 = sqlite3.connect('database.db')
    cur2 = db1.cursor()
    cur2.execute('SELECT integral from solution')
    rows = cur2.fetchall()[Num1][0]
    cur2.close()
    return rows

def ChooseDiffSolution(Num1):
    Num1 = int(Num1)
    db1 = sqlite3.connect('database.db')
    cur2 = db1.cursor()
    cur2.execute('SELECT diffurs from solution')
    rows = cur2.fetchall()[Num1][0]
    cur2.close()
    return rows

def Question(p):
    que = [IntegralQuestion(p), DiffursQuestion(p)]
    return que

def Answer(p):
    que = [IntegralAnswer(p), DiffursAnswer(p)]
    return que

def ChooseSolution(p):
    que = [ChooseIntSolution(p), ChooseDiffSolution(p)]
    return que