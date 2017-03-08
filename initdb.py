import sqlite3

connection = sqlite3.connect('database.db')
print('We\'re connected!')

connection.execute('CREATE TABLE movies (title TEXT, rating INTEGER)')
print('Table created!')

connection.close()
