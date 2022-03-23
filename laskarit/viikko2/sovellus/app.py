from flask import Flask
from random import randint

app = Flask(__name__)

value=randint(1,100)

@app.route("/")
def index():
    return "Satunnainen luku: " + str(value)
