import json

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
def load_data():
    try:
        with open("unit_converter.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"history": {}}

def save_data(data):
    with open("unit_converter.json", "w") as f:
        json.dump(data, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    
    if request.method == "POST":
        
        user_choice = int(request.form.get("choice"))
        val = float(request.form.get("value"))
        
        converter = load_data()
        
        if user_choice == 1:
            res = val * 1000
            key, value = f"{val} KM", f"{res} M"
            converter["history"][key] = value
        elif user_choice == 2:
            res = val / 1000
            key, value = f"{val} M", f"{res} KM"
            converter["history"][key] = value
        elif user_choice == 3:
            res = val / 1000
            key, value = f"{val} G", f"{res} KG"
            converter["history"][key] = value
        elif user_choice == 4:
            res = val * 1000
            key, value = f"{val} KG", f"{res} G"
            converter["history"][key] = value
        elif user_choice == 5:
            res = val * 2.54
            key, value = f"{val} IN", f"{res} CM"
            converter["history"][key] = value
        elif user_choice == 6:
            res = val / 2.54
            key, value = f"{val} CM", f"{res} IN"
            converter["history"][key] = value
        elif user_choice == 7:
            res = (val * 9 / 5) + 32
            key, value = f"{val} C", f"{res} F"
            converter["history"][key] = value
            
        result = f"{key} = {value}"
        
        converter["history"][key] = value
        save_data(converter)
        
    return render_template("index.html", result=result)

@app.route("/edit/<key>", methods=["GET", "POST"])
def edit_record(key):
    converter = load_data()
    if request.method == "POST":
        updated_value = request.form.get("updated_value")

        converter["history"][key] = updated_value
        save_data(converter)

        return redirect(url_for("history"))

    current_value = converter["history"][key]

    return render_template(
        "edit.html",
        key=key,
        current_value=current_value,
    )

@app.route("/history")
def history():
    converter = load_data()
    return render_template("history.html", history=converter["history"])

@app.route("/delete", methods=["POST"])
def delete_record():
    key_to_delete = request.form.get("key")
    converter = load_data()
    
    if key_to_delete in converter["history"]:
        del converter["history"][key_to_delete]
        save_data(converter)
        
    return redirect(url_for("history"))

if __name__ == "__main__":
    app.run(debug=True)