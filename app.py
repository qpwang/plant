#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AUTHOR:   fanzeyi
# CREATED:  15:58:48 20/07/2013
# MODIFIED: 07:21:07 21/07/2013

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/explore')
def explore():
    return render_template("explore.html")

@app.route('/plants')
def plants():
    return render_template("myplant.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

@app.route('/wiki/1')
def wiki1():
    return render_template("wiki1.html")

@app.route('/plant/1')
def plant1():
    return render_template("plant1.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
