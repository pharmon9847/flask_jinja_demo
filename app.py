from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Wyatt_Pepper_Briar'
debug = DebugToolbarExtension(app)


@app.route('/hello')
def say_hello():
    """Shows hello page"""
    return render_template('hello.html')


@app.route('/lucky')
def lucky_number():
    num = randint(1, 100)
    return render_template('lucky.html', lucky_num=num, msg='You are SO lucky!')
