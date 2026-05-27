from flask import Flask, request, render_template
import json

app = Flask(__name__)

# Load Music Data
try:
    with open("music.json", "r") as f:
        music_data = json.load(f)

except FileNotFoundError:
    music_data = {"songs": []}


# Save JSON Function
def save_json():

    with open("music.json", "w") as f:
        json.dump(music_data, f, indent=4)


# Home Route
@app.route("/")
def home():

    return render_template("index.html")


# Recommendation Route
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


# Add Music Route
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

    return render_template(
        "results.html",
        songs=music_data["songs"],
        mood="All Songs"
    )

# Show All Songs
@app.route("/all-songs")
def all_songs():

    try:

        with open("music.json", "r") as f:
            music_data = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):

        music_data = {"songs": []}

    return render_template(
        "results.html",
        songs=music_data["songs"],
        mood="All Songs"
    )

if __name__ == "__main__":
    app.run(debug=True)