from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, st567  ok"
