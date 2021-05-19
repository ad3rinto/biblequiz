from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    return render_template("game.html")

    
app.run(debug=True)
