from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)


@app.route("/", methods=["GET", "POST"])
def notes():
    return render_template("notes.html", notes=Notes.query.all(), mode="list")


@app.route("/add_note_form")
def add_note_form():
    notes_list = Notes.query.all()
    return render_template("notes.html", notes=notes_list, mode="add")


@app.route("/add_note", methods=["GET", "POST"])
def add_note():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        if title:
            note = Notes(title=title, description=description)
            db.session.add(note)
            db.session.commit()
    return redirect(url_for("notes"))


@app.route("/view_notes/<index>")
def view_notes(index):
    notes_list = Notes.query.get(index)
    return render_template("notes.html", note=notes_list, mode="view")


@app.route("/update_note/<index>", methods=["GET", "POST"])
def update_note(index):
    if request.method == "POST":
        notes_list = Notes.query.get(index)
        notes_list.title = request.form.get("title")
        notes_list.description = request.form.get("description")
        db.session.commit()
    return redirect(url_for("notes"))


@app.route("/delete_note/<index>", methods=["POST"])
def delete_note(index):
    if request.method == "POST":
        notes_list = Notes.query.get(index)
        if notes_list:
            db.session.delete(notes_list)
            db.session.commit()
    return redirect(url_for("notes"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
