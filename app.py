from flask import Flask
import json
from datetime import datetime
import random

app = Flask(__name__)

# Calculator

# add


@app.route('/calculator/<int:n>/add/<int:d>')
def add(n, d):
    output = {
        "operation": f'{n} plus {d}',
        "result": n + d
    }
    return json.dumps(output)

# subtract


@app.route('/calculator/<int:n>/subtract/<int:d>')
def subtract(n, d):
    output = {
        "operation": f'{n} minus {d}',
        "result": n - d
    }
    return json.dumps(output)

#  Divide


@app.route('/calculator/<int:n>/divide/<int:d>')
def divide(n, d):
    output = {
        "operation": f'{n} divided by {d}',
        "result": n / d
    }
    return json.dumps(output)

# Multiply


@app.route('/calculator/<int:n>/multiply/<int:d>')
def multiply(n, d):
    output = {
        "operation": f'{n} multiplied by {d}',
        "result": n * d
    }
    return json.dumps(output)


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


@app.route('/some_page/<some_value>')
def some_page(some_value):
    return f"<p>You gave the value {some_value} in the route!</p>"


# Need to have some data to return.
# For a production app this information would be stored in a database of course...
art_dict = {
    "composition 8": {
        "When": "1923",
        "Artist": "Vasily Kandinsky",
        "Medium": "Oil Painting",
        "Place": "Moscow",
        "Periods": ["Suprematism", "Abstract art"]
    },
    "Royal Red and Blue": {
        "When": "1954–1954",
        "Artist": "Mark Rothko",
        "Medium": "Oil Paint",
        "Place": "Litvak Descent",
        "Periods": ["Washington Color School"]
    },
    "Starry Night": {
        "When": "1889",
        "Artist": "Vincent van Gogh",
        "Medium": "Oil Painting",
        "Place": "Netherlands",
        "Periods": ["Post-Impressionism", "Modern art"]
    },
    # ...etc
}


@app.route("/art/<painting_name>")
# """Returns information on a painting in the collection."""
def get_painting(painting_name):

    # If there's no such painting, we return a 404 NOT FOUND error!
    if not painting_name in art_dict:
        abort(404)

    return json.dumps(art_dict[painting_name])


@app.route("/artists/<artist_name>")
# """Returns a list of paintings by a given artist."""
def get_artist(artist_name):
    art_list = []
    for painting in art_dict.values():
        if artist_name == painting["Artist"]:
            art_list.append(painting)

    # If there's no such artist, we return a 404 NOT FOUND error!
    if not art_list:
        abort(404)

    return json.dumps(art_list)

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
