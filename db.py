import random
import sqlite3

connection = sqlite3.Connection("database.db")
cursor = connection.cursor()

cursor.execute('drop table if exists users')
connection.commit()

cursor.execute('create table if not exists Users (id integer primary key ,username text NOT NULL,email not null,age int)')

cursor.execute("create index if not exists idx_email on Users (email)")

# cursor.execute('insert into Users (username, email, age) values (?, ?, ?)', ('newuser', 'ex@gmail.com', 28))
for i in range(30):
    cursor.execute('insert into Users (username, email, age) values (?, ?, ?)', (f'newuser{i}', f'ex{i}@gmail.com', random.randint(20,60)))

cursor.execute('delete from Users where username = ?', ('newuser',))

connection.commit()
connection .close()
