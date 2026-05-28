# app.py
import json
import os
import sqlite3
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///library_managament.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

FILE_NAME = "library.json"

db=SQLAlchemy(app)
migrate=Migrate(app, db)

# ================= DATABASE MODELS =================
class Library(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(100), nullable=False)
    amount=db.Column(db.Float, nullable=False) 

class Books(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    add_book=db.Column(db.String(100),nullable=False)
    author=db.Column(db.String(100),nullable=False)
    cost_amount=db.Column(db.Float,nullable=False)

# ================= LOAD DATA =================
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        library = json.load(f)
else:
    library = {"books": {}}


# ================= HOME =================
@app.route("/")
def home():
    all_books =Books.query.all()
    return render_template("index.html", books=all_books)


# ================= ADD BOOK =================
@app.route("/add", methods=["POST"])
def add_book():
    book_name = request.form["book_name"]
    author = request.form["author"]
    price = request.form["price"]

    new_book = Books(add_book=book_name, author=author, cost_amount=price)
    db.session.add(new_book)
    db.session.commit()
    
    return redirect("/")


# ================= Update BOOK =================
@app.route("/update/<int:book_id>", methods=["POST"])
def update_book(book_id):
    book_to_update = Books.query.get_or_404(book_id)

    old_name = request.form["old_book_name"]
    new_name = request.form["book_name"]
    author = request.form["author"]
    price = request.form["price"]

    book_to_update = Books.query.filter_by(add_book=old_name).first()

    if book_to_update:
        book_to_update.add_book = new_name
        book_to_update.author = author
        book_to_update.cost_amount = price
        db.session.commit()

# ================= DELETE BOOK =================
@app.route("/delete/<int:book_id>")
def delete_book(book_id):

    book_to_delete = Books.query.get_or_404(book_id)
    
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect("/")


# ================= SAVE JSON =================
def save_data():

    with open(FILE_NAME, "w") as f:
        json.dump(library, f, indent=4)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
