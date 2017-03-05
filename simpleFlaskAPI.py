# https://youtu.be/KucNCe_vgcU

from flask import Flask, render_template, request
# 'render_template' renders templates and 'request' handles http requests

import sqlite3

@app.route('/')
def hello_world():
    return render_template(base.html)


