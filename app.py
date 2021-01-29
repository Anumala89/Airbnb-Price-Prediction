from flask import Flask, render_template, redirect, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.static_folder = 'templates/static'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/infographic")
def infographic():
    return render_template("infographic.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)