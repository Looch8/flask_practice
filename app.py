from flask import Flask
import json
from datetime import datetime
import random

app = Flask(__name__)


@app.route('/')
def homepage():
    return """<p>Hi, welcome to my API! Here are the endpoints that are available:</p>
            <ul>
                <li>Current Time: /time</li>
                <li>Educator Info: /educators</li>
            </ul> """


@app.route('/time/')
def current_time():
    time_dict = {"current time": str(datetime.now().strftime('%H:%M'))}
    return json.dumps(time_dict)


@app.route('/educators/')
def educators():
    educator_dict = {
        "educators": [
            {
                "Name": "Oliver",
                "Specialty": "Automated testing"
            },
            {
                "Name": "Jairo",
                "Specialty": "Discrete Mathematics"
            },
            {
                "Name": "Amir",
                "Specialty": "Web Development"
            },
            {
                "Name": "Iryna",
                "Specialty": "Database Engineering"
            },
            {
                "Name": "George",
                "Specialty": "Internet Security"
            },
        ]
    }
    return json.dumps(educator_dict)


@app.route('/coinflip/')
def coinflip():
    choices = ['heads', 'tails']
    result = random.choice(choices)
    coin_dict = {
        "result": result
    }
    return json.dumps(coin_dict)
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# @app.route("/goodbye/")
# def goodbye_world():
#     return "<p>Goodbye, World!</p>"


# @app.route("/coder/")
# def coder():
#     return "<p>This web app was created in a class at Coder Academy</p>"


# @app.route("/current_time/")
# def current_time():
#     date = datetime.now()
#     return str(date)
