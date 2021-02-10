from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fjell.sqlite3'

db = SQLAlchemy(app)


class Fjell(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    navn = db.Column('navn', db.String(100))
    hoyde = db.Column('hoyde', db.Integer)
    bilde = db.Column('bilde', db.String(100))
    kommune = db.Column('kommune', db.String(100))


def __init__(self, navn, hoyde, bilde, kommune):
    self.navn = navn
    self.hoyde = hoyde
    self.bilde = bilde
    self.kommune = kommune


@app.route('/')
def index():
    fjell = db.engine.execute(
        'SELECT * FROM fjell ORDER BY hoyde DESC')

    return render_template('index.html', fjellene=fjell)


@app.route('/liste/<sorter>')
def liste(sorter):
    fjell = db.engine.execute(
        f'SELECT * FROM fjell ORDER BY {sorter} ASC')

    return render_template('liste.html', fjellene=fjell)


@app.route('/fjell/<id>')
def fjell(id):
    fjell = db.engine.execute(
        f'SELECT * FROM fjell WHERE id={id}')

    return render_template('fjell.html', fjellene=fjell)


app.run(debug=True)
