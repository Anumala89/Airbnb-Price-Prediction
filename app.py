from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.static_folder = 'templates/static'

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)