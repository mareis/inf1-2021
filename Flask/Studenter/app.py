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
def index():
    studenter = db.engine.execute('SELECT * FROM studenter')
    return render_template('index.html', studenter=studenter)


@app.route('/ny', methods=['GET', 'POST'])
def ny():
    if request.method == 'POST':
        navn = request.form.get('navn')
        db.engine.execute("INSERT INTO studenter (navn) VALUES(?)", navn)
        return redirect("/")
    return render_template('ny.html')
