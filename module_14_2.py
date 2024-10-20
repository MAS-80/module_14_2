import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Заполняем таблицу
# for i in range(10):
#     n = i+1
#     cursor.execute("INSERT INTO Users (username, email, age, balance)"
#                    "VALUES (?, ?, ?, ?)", (f"User{n}",
#                    f"example{n}@gmail.com", f"{n*10}", "1000"))

# Изменяем у каждого второго баланс с 1000 на 500
# for i in range(10):
#     if i % 2 == 0:
#         n = i + 1
#         cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, f"{n}"))

# # Удаляем каждую третью запись
# for i in range(10):
#     if i % 3 == 0:
#         n = i + 1
#         cursor.execute("DELETE FROM Users WHERE id = ?", (f"{n}",))

# Выборка записей где возраст не 60
# cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[1]}| Почта: {user[2]}| Возраст: {user[3]}| Баланс: {user[4]}')

# Удоляем из базы данных id=6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Подсчет количества всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

# Выводим на консоль средний баланс всех пользователей
print(all_balances/total_users)

connection.commit()
connection.close()
