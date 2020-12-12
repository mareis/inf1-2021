from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hilse/')
def hilse():
    return render_template("hilse.html", navn=request.args.get("navn", "verden"))
