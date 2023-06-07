import sqlite3

conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()


#cur.execute('CREATE TABLE users (login TEXT, passwd TEXT, imie TEXT, nazwisko TEXT, shift TEXT)')

#cur.execute('INSERT INTO users (login, passwd, imie, nazwisko, shift) VALUES (?, ?, ?, ?, ? )',
 #   ('MKOWALSKA', 'HASlO12345', 'MARIA', 'KOWALSKA' ,'B'))

conn.commit()

print('users:')
cur.execute("SELECT * FROM  users ")
for row in cur:
     print(row)

conn.commit()


cur.close()

conn.close()