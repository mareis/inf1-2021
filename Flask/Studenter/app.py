from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studenter.sqlite3'

db = SQLAlchemy(app)


class studenter(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    navn = db.Column(db.String(100))


def __init__(self, navn):
    self.navn = navn


@app.route('/')
def show_all():
    studenter = db.engine.execute('SELECT * FROM studenter')
    return render_template('index.html', studenter=studenter)


@app.route('/ny', methods=['GET', 'POST'])
def ny():
    return render_template('ny.html')
