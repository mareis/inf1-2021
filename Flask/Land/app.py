from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///land.sqlite3'

db = SQLAlchemy(app)

# Tabellen land med tre kolonner (id og navn og befolkning)


class land(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    navn = db.Column('navn', db.String(100))
    befolkning = db.Column('befolkning', db.Integer)


def __init__(self, navn, befolkning):
    self.navn = navn
    self.befolkning = befolkning


@app.route('/')
def index():
    # Henter alle radene og kolonnene i tabellen, land
    land = db.engine.execute('SELECT * FROM land')

    # Sender (land) radene i tabellen til index.html og gjør om til html
    return render_template('index.html', land=land)
