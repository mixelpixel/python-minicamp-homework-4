# https://youtu.be/KucNCe_vgcU

from flask import Flask, render_template, request, jsonify
# 'render_template' renders templates and 'request' handles http requests
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("base.html")







# if __name__ == '__main__':
#     app.run(debug = True)
