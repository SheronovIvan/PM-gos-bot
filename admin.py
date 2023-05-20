import sqlite3
from telebot import types
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('5666049325:AAFjDJSePFY28BtpPPb8adJu8LaAtH5G4AU')
p = 0
admin_id = 572811565
w: str
text: str
text2: str
text3: str
gen = 0

def delete_last_row(table_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name} WHERE ROWID = (SELECT MAX(ROWID) FROM {table_name})")
    conn.commit()
    conn.close()

def delete_last_row_in_column(table_name, column_name, other_column_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table_name} SET {column_name}=null WHERE {other_column_name} IS NOT NULL AND ROWID = (SELECT MAX(ROWID) FROM {table_name} WHERE {column_name})")
    if cursor.rowcount == 0:
        cursor.execute(f"DELETE FROM {table_name} WHERE ROWID = (SELECT MAX(ROWID) FROM {table_name} WHERE {column_name})")
    conn.commit()
    conn.close()

def insert_data_into_table(column1_data, column2_data, table_name, column1, column2):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO {table_name} ({column1}, {column2}) VALUES (?, ?)', (column1_data, column2_data))
    connection.commit()
    connection.close()
'''
def insert_data(column_name, column_value):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE solution SET {column_name} = ? WHERE rowid = (SELECT rowid FROM solution WHERE {column_name} IS NULL ORDER BY rowid LIMIT 1)", (column_value,))
        if cursor.rowcount == 0:
            cursor.execute(f"INSERT INTO solution ({column_name}) VALUES (?)", (column_value,))
        conn.commit()
      '''
def insert_data(column_value, column_name):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT rowid FROM solution WHERE {column_name} IS NULL ORDER BY rowid LIMIT 1")
        row = cursor.fetchone()
        if row:
            rowid = row[0]
            cursor.execute(f"UPDATE solution SET {column_name} = ? WHERE rowid = ?", (column_value, rowid))
        else:
            cursor.execute(f"INSERT INTO solution ({column_name}) VALUES (?)", (column_value,))
        conn.commit()
        conn.close()


def Admin1(cur_call):
    cur_call = None
    markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    intg = types.KeyboardButton('Добавить в Интегралы')
    dif = types.KeyboardButton('Добавить в Диффуры')
    del_intg = types.KeyboardButton('Удалить последний пример из Интегралы')
    del_dif = types.KeyboardButton('Удалить последний пример из Диффуры')
    markup0.add(intg, dif, del_intg, del_dif)
    mess = bot.send_message(chat_id=admin_id, text="Выбирай", reply_markup=markup0)
    bot.register_next_step_handler(mess, Admin2)


def Admin2(message):
    global p
    if message.text == "Добавить в Интегралы":
        msg = bot.send_message(message.chat.id, f"Пиши только сам интеграл")
        bot.register_next_step_handler(msg, Add)
        p = 0
    elif message.text == "Добавить в Диффуры":
        msg = bot.send_message(message.chat.id, f"Пиши только сам диффур")
        bot.register_next_step_handler(msg, Add)
        p = 1
    elif message.text == "Удалить последний пример из Интегралы":
        delete_last_row('users')
        delete_last_row_in_column('solution', 'integral', 'diffurs')
        bot.send_message(message.chat.id, text="Интеграл успешно удален")
    elif message.text == "Удалить последний пример из Диффуры":
        delete_last_row('diffurs')
        delete_last_row_in_column('solution', 'diffurs', 'integral')
        bot.send_message(message.chat.id, text="Диффур успешно удален")

def Add (message):
    global text, text2, text3, gen, w
    if gen == 0:
        text = message.text
        w = text
    if gen == 1:
        text2 = message.text
        w = text2
    if gen == 2:
        text3 = message.text
        w = text3

    button1 = InlineKeyboardButton("Верно", callback_data='1')
    button2 = InlineKeyboardButton("Неверно", callback_data='2')
    markup = InlineKeyboardMarkup().add(button1, button2)
    bot.send_message(message.chat.id, text=f"Вы ввели {w}", reply_markup=markup)


def Ins():
    global gen, p
    if gen == 1:
        msg = bot.send_message(chat_id=admin_id, text="Пиши только сам ответ")
        bot.register_next_step_handler(msg, Add)
    elif gen == 2:
        msg = bot.send_message(chat_id=admin_id, text="Пиши только решение")
        bot.register_next_step_handler(msg, Add)
    elif gen == 3:
        insert(p)

@bot.callback_query_handler(func=lambda call: call.data in ['1', '2'])
def handle_inline_button(call):
    if call.data == '1':
        global gen
        gen += 1
        Ins()
        bot.answer_callback_query(call.id)
    elif call.data == '2':
        gen = 0
        Admin1(call)
        bot.answer_callback_query(call.id)

def insert(p):
       global text, text2, text3

       if p == 0:
            insert_data_into_table(text, text2, 'users', 'questions', 'answers')
            insert_data(text3, 'integral')
       if p == 1:
            insert_data_into_table(text, text2, 'diffurs', 'questions', 'answers')
            insert_data(text3, 'diffurs')
       bot.send_message(chat_id=admin_id, text=f"Вопрос добавлен")