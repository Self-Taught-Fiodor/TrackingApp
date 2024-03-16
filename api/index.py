from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "TODO : HOME PAGE"

@app.route("/login")
def login():
    return "TODO : LOGIN PAGE"

@app.route("/inputs")
def inputs():
    return "TODO : INPUTS PAGE"

@app.route("/resistance")
def resistance():
    return "TODO : RESISTANCE TRAINING PROGRAMME PAGE"

@app.route("/info")
def info():
    return "TODO : PHASES AND LINKS describing them PAGE"

@app.route("/outputs")
def outputs():
    return "TODO : OUTPUTS PAGE select time periode and get back tracked info"
