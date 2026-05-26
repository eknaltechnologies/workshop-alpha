# app.py

from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FILE_NAME = "library.json"

# ================= LOAD DATA =================
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        library = json.load(f)
else:
    library = {"books": {}}

# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html", books=library["books"])


# ================= ADD BOOK =================
@app.route("/add", methods=["POST"])
def add_book():

    book_name = request.form["book_name"]
    author = request.form["author"]
    price = request.form["price"]

    library["books"][book_name] = {
        "author": author,
        "price": price
    }

    save_data()

    return redirect("/")

# ================= Update BOOK =================
@app.route("/update", methods=["POST"])
def update_book():
    old_name = request.form["old_book_name"]   
    new_name = request.form["book_name"]
    author = request.form["author"]
    price = request.form["price"]

    if old_name in library["books"] and old_name != new_name:
        del library["books"][old_name]          

    library["books"][new_name] = {
        "author": author,
        "price": price
    }

    save_data()
    return redirect("/")


# ================= DELETE BOOK =================
@app.route("/delete/<book_name>")
def delete_book(book_name):

    if book_name in library["books"]:
        del library["books"][book_name]

    save_data()

    return redirect("/")


# ================= SAVE JSON =================
def save_data():

    with open(FILE_NAME, "w") as f:
        json.dump(library, f, indent=4)


if __name__ == "__main__":
    app.run(debug=True)