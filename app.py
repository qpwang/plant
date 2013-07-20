#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AUTHOR:   fanzeyi
# CREATED:  15:58:48 20/07/2013
# MODIFIED: 19:04:15 20/07/2013

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/explore')
def explore():
    return render_template("explore.html")

if __name__ == '__main__':
    app.run()
