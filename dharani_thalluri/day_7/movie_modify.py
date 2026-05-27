import json

from flask import Flask, render_template, request

app = Flask(__name__)

try:

    with open("movies.json", "r") as f:

        movie_data = json.load(f)

except FileNotFoundError:

    movie_data = {"movies": []}


def save_json():

    with open("movies.json", "w") as f:

        json.dump(movie_data, f, indent=4)


@app.route("/")
def home():

    return render_template("home.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    selected_mood = request.form.get("mood")

    result = []

    for movie in movie_data["movies"]:

        if movie["mood"].lower() == selected_mood.lower():

            result.append(movie)

    return render_template("result.html", movies=result, mood=selected_mood)


@app.route("/add-movie", methods=["POST"])
def add_movie():

    new_movie = {
        "name": request.form.get("name"),
        "genre": request.form.get("genre"),
        "mood": request.form.get("mood"),
        "emoji": request.form.get("emoji"),
        "poster": request.form.get("poster"),
    }

    movie_data["movies"].append(new_movie)

    save_json()

    return render_template("home.html")


if __name__ == "__main__":

    app.run(debug=True)
