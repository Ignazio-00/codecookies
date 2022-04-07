from crypt import methods
from re import T
from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)
app.config.from_object('app.config')

cookies_data = [
  {'name': 'Chocolate Chip', 'price': '$1.50'},
  {'name': 'Oatmeal Raisin', 'price': '$1.00'},
  {'name': 'Sugar', 'price': '$0.75'},
  {'name': 'Peanut Butter', 'price': '$0.50'},
  {'name': 'Oatmeal', 'price': '$0.25'},
  {'name': 'Salted Caramel', 'price': '$1.00'},
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/cookies/<int:id>")
def cookie(id):
    return "<h1>" + cookies_data[id]["name"] + "</h1>" + "<p>" + cookies_data[id]["price"] + "</p>"

