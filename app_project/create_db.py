import sqlite3

conn = sqlite3.connect('database.db')
print('Opened database Successfully')

conn.execute('CREATE TABLE USER (ID PRIMARY KEY, PW PRIMARY KEY)')
print('Table created successfully')
conn.close()