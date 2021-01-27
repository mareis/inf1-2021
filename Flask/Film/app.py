from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///film.sqlite3'

db = SQLAlchemy(app)

# Tabellen land med tre kolonner (id og navn og befolkning)


class filmer(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    tittel = db.Column('tittel', db.String(255))
    terningkast = db.Column('terningkast', db.Integer)
    aar = db.Column('aar', db.Integer)


def __init__(self, tittel, terningkast, aar):
    self.tittel = tittel
    self.terningkast = terningkast
    self.aar = aar


@app.route('/')
def index():
    # Henter alle radene og kolonnene i tabellen, filmer.
    filmer = db.engine.execute(
        'SELECT * FROM filmer ORDER BY terningkast DESC')

    # Sender (filmer) radene i tabellen til index.html og gjør om til html
    return render_template('index.html', filmer=filmer)
