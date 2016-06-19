#!/usr/bin/env python

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['POST'])
def process_text():
    return 'Response from backend'

@app.route('/solutions', methods=['GET'])
def solutions():
    return 'answers' 
