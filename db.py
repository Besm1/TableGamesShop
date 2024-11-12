import random
import sqlite3

connection = sqlite3.Connection("database.db")
cursor = connection.cursor()

# cursor.execute('drop table if exists Users_Test')
# connection.commit()
#
# cursor.execute('create table if not exists Users_Test (id integer primary key ,username text NOT NULL,email not null,age int)')
#
# cursor.execute("create index if not exists idx_email on Users_Test (email)")
#
# # cursor.execute('insert into Users_Test (username, email, age) values (?, ?, ?)', ('newuser', 'ex@gmail.com', 28))
# for i in range(30):
#     cursor.execute('insert into Users_Test (username, email, age) values (?, ?, ?)', (f'newuser{i}', f'ex{i}@gmail.com', random.randint(20,60)))
#
# cursor.execute('delete from Users_Test where username = ?', ('newuser',))

cursor.execute('select max(age) from users')
print(cursor.fetchall(), cursor.fetchall())



connection.commit()
connection.close()
