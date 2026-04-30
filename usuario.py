from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index1():
    return render_template("index1.html")

@app.route("/login")
def index2():
    return render_template("index2.html")

@app.route("/alunos")
def index3():
    return render_template("index3.html")

if __name__ == "__main__":
    app.run()