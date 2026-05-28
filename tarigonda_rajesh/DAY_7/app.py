from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///converter.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Convert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_value = db.Column(db.String(20), nullable=False)
    output_value = db.Column(db.String(20), nullable=False)
    conversion_type = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":

        user_choice = int(request.form.get("choice"))
        val = float(request.form.get("value"))

        if user_choice == 1:
            res = val * 1000
            input_val = f"{val} KM"
            output_val = f"{res} M"
            conversion_type = "Length"

        elif user_choice == 2:
            res = val / 1000
            input_val = f"{val} M"
            output_val = f"{res} KM"
            conversion_type = "Length"

        elif user_choice == 3:
            res = val / 1000
            input_val = f"{val} G"
            output_val = f"{res} KG"
            conversion_type = "Weight"

        elif user_choice == 4:
            res = val * 1000
            input_val = f"{val} KG"
            output_val = f"{res} G"
            conversion_type = "Weight"

        elif user_choice == 5:
            res = val * 2.54
            input_val = f"{val} IN"
            output_val = f"{res} CM"
            conversion_type = "Height"

        elif user_choice == 6:
            res = val / 2.54
            input_val = f"{val} CM"
            output_val = f"{res} IN"
            conversion_type = "Height"

        elif user_choice == 7:
            res = (val * 9 / 5) + 32
            input_val = f"{val} C"
            output_val = f"{res} F"
            conversion_type = "Temperature"

        data = Convert(
            input_value=input_val, 
            output_value=output_val, 
            conversion_type=conversion_type, 
            created_at=datetime.now()
        )
        db.session.add(data)
        db.session.commit()
        result = f"{input_val} = {output_val}"

    return render_template("index.html", result=result)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_record(id):
    record = Convert.query.get_or_404(id)

    if request.method == "POST":
        updated_value = request.form.get("updated_value")
        record.output_value = updated_value
        db.session.commit()

        return redirect(url_for("history"))

    return render_template("edit.html", record=record), 400


@app.route("/history")
def history():
    records = Convert.query.all()
    return render_template("history.html", history=records)


@app.route("/delete/<int:id>", methods=["POST"])
def delete_record(id):
    record = Convert.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for("history"))


if __name__ == "__main__":
    app.run(debug=True)
