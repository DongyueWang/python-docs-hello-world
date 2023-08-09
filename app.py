from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, 123  ok"
