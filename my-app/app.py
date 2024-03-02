from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello SkillUp Club" 

@app.route("/bye")
def bye():
    return "Bye..." 

@app.route("/interesting")
def interesting():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()