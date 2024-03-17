from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

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

if __name__ == "__main__":
    app.run(debug=True)