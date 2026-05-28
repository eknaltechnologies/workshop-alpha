from flask import Flask, request

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return "Welcome to Home Page"


@app.route("/about")
def about():
    return "Welcome to About Page"


@app.route("/contact")
def contact():
    return "Welcome to Contact Page"


@app.route("/pari")
def pari():
    return """
    <h1>This is Pari</h1>
    <p>I am currently working in an MNC company.
    It is very grateful to work in this company.</p>
    """


@app.route("/students", methods=["GET", "POST", "DELETE"])
def student_operations():

    if request.method == "POST":
        name = request.form.get("name")

        if not name:
            return "Please enter a student name"

        students.append(name)
        return f"{name} added successfully"

    if request.method == "DELETE":

        if students:
            deleted_student = students.pop()
            return f"{deleted_student} deleted successfully"

        return "No students found"

    return {"students": students}


if __name__ == "__main__":
    app.run(debug=True, port=5000)