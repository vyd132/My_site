import random,sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def index():
    buttons=[name for name in range(1,28)]
    return render_template("main.html", title="Моё приложение", buttons=buttons, tasktext=[])

@app.route("/topic")
def topic():
    base = sqlite3.connect("DB/db")
    c = base.cursor()
    num = request.args.get("num", default=1, type=int)
    text=c.execute(f"""
        SELECT text
        FROM egetask 
        WHERE tasknumber={num}
    """)
    buttons = [name for name in range(1, 28)]
    return render_template("main.html", title="Моё приложение", buttons=buttons, num=num, tasktext=[x for x in text])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)