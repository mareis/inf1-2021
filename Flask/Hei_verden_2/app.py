from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)


class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))


def __init__(self, name):
    self.name = name


@app.route('/')
def show_all():
    students = db.engine.execute('SELECT * FROM students')
    return render_template('show_all.html', students=students)


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        name = request.form.get('name')
        db.engine.execute("INSERT INTO students (name) VALUES(?)", name)
        return redirect("/")

    return render_template('new.html')
