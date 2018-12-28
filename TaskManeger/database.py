import sqlite3
 
db = sqlite3.connect("database.db") 
cursor = db.cursor()
 
cursor.execute("""CREATE TABLE tasks (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name text, description text, groups text, date_v text, time_v text)""")

cursor.execute("INSERT INTO tasks (name, description, groups, date_v, time_v) VALUES ('Погулять', 'выйти на улицу и погулять', 'important', '27.12.2018', '19.00')")

db.commit()