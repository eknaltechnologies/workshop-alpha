from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def notes():
    return """
     <center><h1>Welcome to Notes App</h1></center>
     <h2>Add calculator or notes/name/note_title to IP to select an option</h2>
    <h2>1.Simple calculator</h2>
    <h2>2.Notes app</h2>"""

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
     num1 = request.form.get("num1")
     num2 = request.form.get("num2")
     operator = request.form.get("operator")
     result=" "
     if num1 and num2 and operator:
         num1 = int(num1)
         num2 = int(num2)
         if operator == "+":
             result = num1 + num2
         elif operator == "-":
             result = num1 - num2
         elif operator == "*":
             result = num1 * num2
         elif operator == "/":
             result = num1 / num2
    
     return f"""<center><form method="post">

    <input type="number" name="num1">

    <input type="number" name="num2">

    <select name="operator">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
    </select>

    <button type="submit">Calculate</button>

     </form>
     <h1>Result: {result}</h1>
    </center>"""

@app.route("/notes/<name>")
def welcome(name):
    return f"""<center><h1>Welcome to Notes App {name}</h1></center>"""

@app.route("/notes/<name>/<note_title>")
def about(note_title):
    return f"""
    <h1>The title of note is: {note_title}</h1>
    <textarea placeholder="Enter your note here..."></textarea>
     """
if __name__=="__main__":
    app.run(debug=True)


