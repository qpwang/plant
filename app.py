#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AUTHOR:   fanzeyi
# CREATED:  15:58:48 20/07/2013
# MODIFIED: 23:05:34 20/07/2013

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

if __name__ == '__main__':
    app.run()
