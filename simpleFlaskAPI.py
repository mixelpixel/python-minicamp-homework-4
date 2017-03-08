# https://youtu.be/KucNCe_vgcU

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# The following is as opposed to externally creating an initdb.py script and
# manually entering `python3 initdb.py` in a python3 interpreter
# e.g.
# import sqlite3
# connection = sqlite3.connect('database.db')
# print('We\'re connected!')
# connection.execute('CREATE TABLE movies (title TEXT, rating INTEGER)')
# print('Table created!')
# connection.close()
####################
# This is also a nice solution to manually creating the database using an
# an external initdb.py script:
#
# from os.path import isfile
# @app.route('/')
# def index():
#     if isfile('database.db') == False:
#         exec(open('initdb.py').read())
#     return render_template('base.html')
####################
#
# connecting application to the database
connection = sqlite3.connect('database.db')
print('Database opened successfully')
# execute database commands - NOTE: the if not exists check
connection.execute('CREATE TABLE IF NOT EXISTS movies (title TEXT, rating INTEGER)')
print('Table created successfully')
# close database connection
connection.close()
print('database closed')

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/movie_added', methods = ['POST'])
def movie_added():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    print("1>>>HELLO????")

    title = request.form['title']
    print("2>>>HELLO????")
    rating = request.form['rating']
    print("3>>>HELLO????")
    try:
        print('a')
        cursor.execute('INSERT INTO movies (title, rating) VALUES (?, ?)', (title, rating))
        print('b')
        connection.commit()
        print('c')
        message = 'Successfully inserted title and rating data into movies table!'
    except:
        connection.rollback()
        message = 'There was an issue with inserting data into the movies table :('
    finally:
        connection.close()
        return message

app.run(debug = True)
# if __name__ == '__main__':
#     app.run(debug = True)
