# https://youtu.be/KucNCe_vgcU
# SQLite Viewer: http://inloop.github.io/sqlite-viewer/

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# The following is as opposed to externally creating an initdb.py script and
# manually entering `python3 initdb.py` in a python3 interpreter
# e.g. the initdb.py file would read:
# import sqlite3
# connection = sqlite3.connect('database.db')
# connection.execute('CREATE TABLE movies (title TEXT, rating INTEGER)')
# connection.close()
####################
# This is also a nice alternative to manually creating the database using
# the aboove external initdb.py script with the following code here:
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
# execute database commands - note the if not exists check, nice!
connection.execute('CREATE TABLE IF NOT EXISTS films (title TEXT, rating INTEGER)')
# close database connection
connection.close()

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/movie', methods = ['POST'])
def add_movie_function():
    connection  = sqlite3.connect('database.db')
    cursor      = connection.cursor()
    title       = request.form['title']
    rating      = request.form['rating']
    try:
        query   = 'INSERT INTO films (title, rating) VALUES (?, ?)'
        cursor.execute(query, (title, rating))
        connection.commit()
        message = 'Successfully inserted title and rating data into movies table!'
    except:
        connection.rollback()
        message = 'There was an issue with inserting data into the movies table :('
    finally:
        connection.close()
        return message

@app.route('/movies', methods = ['GET'])
def list_all_movies():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM films')
    search_result = jsonify(cursor.fetchall())
    connection.close()
    return search_result

#####################################
# # Looks like I don't need all this try/except/finally
# # Also not sure what connection.commit() is for?
#
# @app.route('/movies', methods = ['GET'])
# def list_all_movies():
#     connection = sqlite3.connect('database.db')
#     cursor = connection.cursor()
#     try:
#         cursor.execute('SELECT * FROM films')
#         connection.commit()
#         search_result = jsonify(cursor.fetchall())
#     except:
#         search_result = 'An error occured getting all the film titles'
#     finally:
#         connection.close()
#         return search_result

#######################################
# # While getting an error upon exiting the flask server
# # I tried the following to see if the error was the result
# # of how I was closing out connections
#
# @app.route('/movie', methods = ['POST'])
# def add_movie_function():
#     data = None
#     try:
#         connection  = sqlite3.connect('database.db')
#         with connection:
#             cursor      = connection.cursor()
#             title       = request.form['title']
#             rating      = request.form['rating']
#             query   = 'INSERT INTO films (title, rating) VALUES (?, ?)'
#             data = cursor.execute(query, (title, rating))
#             connection.commit()
#             message = 'Successfully inserted title and rating data into movies table!'
#     except sqlite3.Error as e:
#         if connection:
#             connection.rollback()
#             message = 'There was an issue with inserting data into the movies table :('
#         raise ValueError('sqlite3: {}'.format(e))
#     finally:
#         if connection:
#             connection.close()
#             print(message)
#         if data:
#             print(data)
#             return message
#
# @app.route('/movies', methods = ['GET'])
# def list_all_movies():
#     data = None
#     try:
#         connection = sqlite3.connect('database.db')
#         with connection:
#             cursor = connection.cursor()
#             data = cursor.execute('SELECT * FROM films')
#             connection.commit()
#             search_result = jsonify(cursor.fetchall())
#     except sqlite3.Error as e:
#         if connection:
#             search_result = 'An error occured getting all the film titles'
#         raise ValueError('sqlite3: {}'.format(e))
#     finally:
#         if connection:
#             connection.close()
#             print(search_result)
#         if data:
#             print(data)
#             return search_result



app.run(debug = True)
# if __name__ == '__main__':
#     print('__name__ == "__main__"')
#     app.run(debug = True)
