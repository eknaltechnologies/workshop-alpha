from flask import Flask, request, render_template
import json

app = Flask(__name__)

try:
    with open("music.json", "r") as f:
        music_data = json.load(f)
except FileNotFoundError:
    music_data = {"songs": []}



def save_json():
    with open("music.json", "w") as f:
        json.dump(music_data, f, indent=4)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend_music():

    selected_mood = request.form.get("mood")

    recommended_songs = []

    for song in music_data["songs"]:

        if song["mood"].lower() == selected_mood.lower():

            recommended_songs.append(song)

    return render_template(
        "results.html",
        songs=recommended_songs,
        mood=selected_mood
    )



@app.route("/add-music", methods=["POST"])
def add_music():

    new_song = {
        "name": request.form.get("name"),
        "artist": request.form.get("artist"),
        "mood": request.form.get("mood"),
        "emoji": request.form.get("emoji"),
        "poster": request.form.get("poster")
    }

    music_data["songs"].append(new_song)

    save_json()

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)