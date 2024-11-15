import sqlite3

connection = sqlite3.Connection("not_telegram.db")
cursor = connection.cursor()

cursor.execute('drop table if exists users')
connection.commit()

cursor.execute('''
create table if not exists Users (
id integer primary key
, username text NOT NULL
, email not null
, age integer
, balance integer)
''')

for i in range(1, 11):
    cursor.execute('insert into Users (username, email, age, balance) values (?, ?, ?, ?)',
                   (f'newuser{i}', f'example{i}@gmail.com', 10*i, 1000))

cursor.execute('update users set balance = 500 where id % 2 = 1')
cursor.execute('delete from users where (id - 1) % 3 = 0')
cursor.execute('select username, email, age, balance from Users where age <> 60')
recs = cursor.fetchall()
f_names =  ['Имя', 'Почта', 'Возраст', 'Баланс']
for rec_ in recs:
    for i in range(4):
        print(f'{f_names[i]}: {rec_[i]}', end='\t| ')
    print(rec_)

cursor.execute('delete from users where id = 6')
connection.commit()

cursor.execute('select count(*), sum(balance), avg(balance) from users')
total_users, total_balance, avg_balance = cursor.fetchall()[0]
print(f'Всего юзверей: {total_users}')
print(f'Всего на счетах: {total_balance}')
print(f'Средний баланс: {total_balance / total_users}')
print(f'Средний баланс (из ф-ции AVG): {avg_balance}')


connection .close()
