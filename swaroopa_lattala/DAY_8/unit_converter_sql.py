from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///converter.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conversion_type = db.Column(db.String(50), nullable=False)
    input_value = db.Column(db.String(100), nullable=False)
    result_value = db.Column(db.String(100), nullable=False)


def __repr__(self):
    return f"<History {self.input_value}>"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        user_choice = int(request.form.get("choice"))
        val = float(request.form.get("value"))

        if user_choice == 1:
            res = val * 1000
            key = f"{val} KM"
            value = f"{res} M"
            conversion_type = "Length"

        elif user_choice == 2:
            res = val / 1000
            key = f"{val} M"
            value = f"{res} KM"
            conversion_type = "Length"

        elif user_choice == 3:
            res = val / 1000
            key = f"{val} G"
            value = f"{res} KG"
            conversion_type = "Weight"

        elif user_choice == 4:
            res = val * 1000
            key = f"{val} KG"
            value = f"{res} G"
            conversion_type = "Weight"

        elif user_choice == 5:
            res = val * 2.54
            key = f"{val} IN"
            value = f"{res} CM"
            conversion_type = "Length"

        elif user_choice == 6:
            res = val / 2.54
            key = f"{val} CM"
            value = f"{res} IN"
            conversion_type = "Length"

        elif user_choice == 7:
            res = (val * 9 / 5) + 32
            key = f"{val} C"
            value = f"{res} F"
            conversion_type = "Temperature"
        new_record = History(conversion_type=conversion_type, input_value=key, result_value=value)
        db.session.add(new_record)
        db.session.commit()
        result = f"{key} = {value}"

    return render_template("index.html", result=result)


@app.route("/history")
def history():
    records = History.query.all()
    return render_template("history.html", history=records)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_record(id):
    record = History.query.get_or_404(id)

    if request.method == "POST":
        updated_value = request.form.get("updated_value")
        record.result_value = updated_value
        db.session.commit()
        return redirect(url_for("history"))

    return render_template("edit.html", record=record)


@app.route("/delete/<int:id>", methods=["POST"])
def delete_record(id):
    record = History.query.get(id)
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for("history"))


if __name__ == "__main__":
    app.run(debug=True)
