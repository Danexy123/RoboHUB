from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("base.html")

@app.route('/about/quadcopter')
def base1():
    return render_template("quadcopter.html")

@app.route('/about/uno_car')
def base2():
    return render_template("uno_car.html")

@app.route('/about/manipulator')
def base3():
    return render_template("manipulator.html")


if __name__ == "__main__":
    app.run(debug=True)