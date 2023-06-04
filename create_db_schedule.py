import sqlite3

conn = sqlite3.connect('schedule.sqlite')
cur = conn.cursor()


#cur.execute('CREATE TABLE schedule (SHIFT TEXT, year INT, month INT, day INT)')

cur.execute('INSERT INTO schedule (shift, year, month, day ) VALUES (?, ?, ?, ? )',
    ('B', 2023, 5, 1))

conn.commit()

print('grafik:')
cur.execute('SELECT * from schedule')
for row in cur:
     print(row)

conn.commit()


cur.close()

