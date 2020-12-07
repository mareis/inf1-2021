from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hei, verden!"


@app.route("/navn")
def navn():
    return f"Hei, !"
