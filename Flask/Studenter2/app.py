from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studenter.sqlite3'

db = SQLAlchemy(app)


# Tabellen studenter med to kolonner (id og navn)
class studenter(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    navn = db.Column(db.String(100))


def __init__(self, navn):
    self.navn = navn


@app.route('/')
def index():
    # Henter alle radene og kolonnene i tabellen, studenter
    studenter = db.engine.execute('SELECT * FROM studenter')

    # Sender (studenter) radene i tabellen til index.html og gjør om til html
    return render_template('index.html', studenter=studenter)


@app.route('/filter')
def filter():
    # Henter alle radene og kolonnene i tabellen, studenter
    studenter = db.engine.execute('SELECT * FROM studenter WHERE navn="Peach"')

    # Sender (studenter) radene i tabellen til index.html og gjør om til html
    return render_template('index.html', studenter=studenter)
