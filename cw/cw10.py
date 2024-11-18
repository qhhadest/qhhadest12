#import sqlite3

#connection = sqlite3.connect("itstep.sl13", timeout=5)

#cur = connection.cursor()
#cur.execute("""CREATE TABLE IF NOT EXISTS first_table (name TEXT);""")
#cur.execute("""INSERT INTO first_table (name) VALUES ('Nick');  """)
#cur.execute("""UPDATE first_table SET name = "Kate" Where rowid = 3""")
#cur.execute("SELECT rowid, name FROM first_table;")

#cur.execute("Delete FROM first_table WHERE rowid = 1;")
#cur.execute("SELECT rowid, name FROM first_table;")


#connection.commit() # save
#res = cur.fetchall()
#print(res)
#connection.close()
import sqlite3


# Підключення до бази даних
conn = sqlite3.connect('ShopDB.sqlite')
cursor = conn.cursor()


def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        FullName TEXT NOT NULL,
        Email TEXT UNIQUE NOT NULL,
        PasswordHash TEXT NOT NULL,
        RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Description TEXT,
        Price REAL NOT NULL,
        Stock INTEGER DEFAULT 0
    )
    ''')
    conn.commit()


def add_user(full_name, email, password):
    if full_name and email and password:
        try:
            cursor.execute('''
            INSERT INTO Users (FullName, Email, PasswordHash) VALUES (?, ?, ?)
            ''', (full_name, email, password))
            conn.commit()
            print("Користувач доданий успішно!")
        except sqlite3.IntegrityError:
            print("Помилка: email уже існує!")
    else:
        print("Заповніть усі поля!")


def add_product(name, description, price, stock):
    try:
        cursor.execute('''
        INSERT INTO Products (Name, Description, Price, Stock) VALUES (?, ?, ?, ?)
        ''', (name, description, price, stock))
        conn.commit()
        print("Продукт доданий успішно!")
    except ValueError:
        print("Помилка: введіть коректні дані!")


def view_table(table_name):
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("Таблиця порожня.")
    except sqlite3.OperationalError:
        print("Таблиця не існує.")


def main():
    create_tables()

    while True:
        print("\nМенеджер бази даних")
        print("1. Додати користувача")
        print("2. Додати продукт")
        print("3. Переглянути таблицю")
        print("4. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            full_name = input("Повне ім'я: ")
            email = input("Email: ")
            password = input("Пароль: ")
            add_user(full_name, email, password)
        elif choice == '2':
            name = input("Назва: ")
            description = input("Опис: ")
            price = float(input("Ціна: "))
            stock = int(input("Кількість: "))
            add_product(name, description, price, stock)
        elif choice == '3':
            table_name = input("Назва таблиці (Users або Products): ")
            view_table(table_name)
        elif choice == '4':
            break
        else:
            print("Невірний вибір, спробуйте знову.")

    conn.close()


if __name__ == "__main__":
    main()
