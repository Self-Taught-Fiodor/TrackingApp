from flask import Flask, render_template, redirect, url_for, request
#from forms import SignUpForm

app = Flask(__name__)
#app.config["SECRET_KEY"] = "7V89?-_uPQkSLKss"

@app.route("/")
def redirect_landing():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home2.html", show_nav=True)

#@app.route("/signup")
#def signup():
#    form = SignUpForm()
#    return render_template("signup.html", form=form)

@app.route("/login")
def login():
    return render_template("login.html", show_nav=True)

@app.route("/inputs")
def inputs():
    return render_template("inputs.html", show_nav=True)

@app.route("/resistance")
def resistance():
    return render_template("resistance.html", show_nav=True)

@app.route("/info")
def info():
    return render_template("info.html", show_nav=True)

@app.route("/outputs")
def outputs():
    return render_template("outputs.html", show_nav=True)

if __name__ == "__main__":
    app.run(debug=True)