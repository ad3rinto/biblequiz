
from flask import Flask, render_template, request
import quiz


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/play", methods=["GET", "POST"])
@app.route('/game_backup', methods=["GET","POST"])
def play():
    if request.method == "POST":
        return render_template("game_backup.html", question=quiz.questions)
        # Process submitted answer
    else:
        #s
# return redirect("play.html", question=quiz.questions)


app.run(debug=True)
