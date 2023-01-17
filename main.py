from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/about_cosmyc_arcade", methods=["POST", "GET"])
def about_cosmyc_arcade():
    return render_template("aboutcosmycarcade.html")


@app.route("/CosMycArcade")
def play_cosmycarcade():
    return render_template("CosMyc.html")


if __name__ == "__main__":
    app.run()
