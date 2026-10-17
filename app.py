import random

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    buttons=[name for name in range(1,28)]
    return render_template("main.html", title="Моё приложение", buttons=buttons)

@app.route("/topic")
def topic():
    num = request.args.get("num", default=1, type=int)
    buttons = [name for name in range(1, 28)]
    return render_template("main.html", title="Моё приложение", buttons=buttons, num=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)