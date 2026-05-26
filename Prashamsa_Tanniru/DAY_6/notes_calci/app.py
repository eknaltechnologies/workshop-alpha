from flask import Flask, render_template, request , redirect , url_for
import json
app = Flask(__name__)
notes_files = "notes.json" 

def load_notes(): 
    try:
      with open(notes_files,"r") as f:
        return json.load(f)
    except (FileNotFoundError,KeyboardInterrupt):
        return []
def save_notes(notes):
    with open(notes_files,"w") as f:
        json.dump(notes,f)  
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/calculator", methods=["GET","POST"])
def calculator():
    result = " "
    if request.method == "POST":
     num1 = request.form.get("num1")
     num2 = request.form.get("num2")
     operator = request.form.get("operator")
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
            if num2 == 0:
             result = "Error: Division by zero"
            else:
                result = num1 / num2
    return render_template("calculator.html", result=result)

@app.route("/notes", methods=["GET","POST"])
def notes():
    notes_list = load_notes()
    return render_template("notes.html", notes=notes_list, mode="list")

@app.route("/add_note_form")
def add_note_form():
    notes_list = load_notes()
    return render_template("notes.html", notes=notes_list, mode="add")

@app.route("/add_note",methods=["GET","POST"])
def add_note():
    notes_list = load_notes()
    title= request.form.get("title")
    description = request.form.get("description")
    if title:
        notes_list.append({"title": title, "description": description})
        save_notes(notes_list)  
    return redirect(url_for("home")) 

@app.route("/view_notes/<index>")
def view_notes(index):
    notes_list = load_notes()
    if 0 <= int(index) < len(notes_list):
        return render_template("notes.html", notes=notes_list, note=notes_list[int(index)], index=index, mode="view")
    return redirect(url_for("home"))

@app.route("/update_note/<index>", methods=["GET","POST"])
def update_note(index):
    if request.method == "POST":
        notes_list = load_notes()
        if 0 <= int(index) < len(notes_list):
          title = request.form.get("title")
          description = request.form.get("description")
          notes_list[int(index)] = {"title": title, "description": description}
          save_notes(notes_list)
    return redirect(url_for("home"))

@app.route("/delete_note/<index>", methods=["POST"])
def delete_note(index):
    if request.method == "POST":
        notes_list = load_notes()
        if 0 <= int(index) < len(notes_list):
            notes_list.pop(int(index))
            save_notes(notes_list)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)