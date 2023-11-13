from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Wyatt_Pepper_Briar'
debug = DebugToolbarExtension(app)

COMPLIMENTS = ["bad ass!", "stellar!", "fucking awesome!",
               "most righteous!", "killer!", "on point!"]


@app.route('/hello')
def say_hello():
    """Shows hello page"""
    return render_template('hello.html')

@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')


@app.route('/lucky')
def lucky_number():
    num = randint(1, 10)
    return render_template('lucky.html', lucky_num=num, msg='You are SO lucky!')


@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/greet')
def get_greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment=nice_thing)


@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)


@app.route('/form-2')
def show_form_2():
    return render_template('form-2.html')


@app.route('/greet-2')
def get_greeting_2():
    username = request.args["username"]
    wants = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet_2.html', username=username, wants_compliments=wants, compliments=nice_things)
