import sqlite3
from random import randint
global db
global sql
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS USERS (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

db.commit()
def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_password, 0))
        db.commit()

        print('Зарегистрировано')
    else:
        print('Такая запись уже имеется!')

        for value in sql.execute("SELECT * FROM users"):
            print(value)

def delete_db():
    sql.execute(f"DELETE FROM users WHERE login = '{user_login}:'")
    sql.execute(f"DELETE FROM users WHERE password = '{user_password}:'")
    db.commit()

    print('Запись удалена!')

def casino():
    global user_login
    global user_password
    user_login = input("Log in: ")
    user_password = input("Take password: ")
    number = randint(1, 2)

    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
        balance = i[0]

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print('Такого логина не существует. Зарегистрируйтесь!')
        reg()
    else:
        sql.execute(f'SELECT password FROM users WHERE password = "{user_password}"')
        if sql.fetchone() is None:
            print('Неверный пароль')
            return
        else:
            if number == 1:
                print('Вы выиграли!')
                sql.execute(f'UPDATE users SET cash = {1000 + balance} WHERE login  = "{user_login}"')
                db.commit()
                enter()
            else:
                print('Вы проиграли!')
                delete_db()
def enter():
    for i in sql.execute('SELECT login, cash FROM users'):
        print(i)

def main():
    casino()

main()
