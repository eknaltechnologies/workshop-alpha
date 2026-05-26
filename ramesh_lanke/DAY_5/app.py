from flask import Flask, request, render_template
import json

app = Flask(__name__)



try:
    with open("expenses.json", "r") as f:
        expense_list = json.load(f)
except FileNotFoundError:
    expense_list = {"expenses": {}}



def save_json(expense_list):
    with open("expenses.json", "w") as f:
        json.dump(expense_list, f)

@app.route('/', methods=['GET', "POST"])
def home():
    return render_template("home.html")


@app.route("/add-expense", methods=["POST", "GET"])
def add_expense():
    if request.method == "POST":
        print(request.form)
        amount = request.form.get("amount")
        desc = request.form.get("description")
        print(amount, desc)
        expense_list["expenses"][desc] = amount
        save_json(expense_list)
        return render_template("home.html")
    return render_template("add-expense.html")


@app.route("/view-expenses", methods=["GET"])
def view_expenses():
    print(expense_list["expenses"])
    for desc, amount in expense_list["expenses"].items():
        print(desc, amount)
    return render_template("view-expenses.html", context=expense_list["expenses"])


@app.route("/update-expense", methods=["GET"])
def update_expenses():
    print(expense_list["expenses"])
    for desc, amount in expense_list["expenses"].items():
        print(desc, amount)
    return render_template("update-expense.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)