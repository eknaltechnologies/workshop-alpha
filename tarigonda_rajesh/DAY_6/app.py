from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


# Load JSON Data

try:
    with open("music_list.json", "r") as f:
        music_list = json.load(f)

except FileNotFoundError:
    music_list = {}


# Save Data Function


def save_data():
    with open("music_list.json", "w") as f:
        json.dump(music_list, f, indent=4)


# Dashboard Route


@app.route("/")
def dashboard():
    total_songs = len(music_list)

    favorite_count = 0

    favorite_songs = {}

    albums = set()

    genres = set()

    for song, details in music_list.items():
        albums.add(details["album"])

        genres.add(details["genre"])

        if details["favorite"]:
            favorite_count += 1

            favorite_songs[song] = details

    recent_songs = list(music_list.items())[-5:]

    return render_template(
        "dashboard.html",
        total_songs=total_songs,
        favorite_count=favorite_count,
        album_count=len(albums),
        genre_count=len(genres),
        recent_songs=recent_songs,
        favorite_songs=favorite_songs,
        genres_list=genres,
    )


# Songs Page


@app.route("/songs")
def songs():
    search = request.args.get("song", "").lower()

    filtered_songs = {}

    for song, details in music_list.items():
        if search in song.lower() or search in details["singer"].lower():
            filtered_songs[song] = details

    return render_template("songs.html", music_list=filtered_songs)


# Add Song


@app.route("/add-song", methods=["GET", "POST"])
def add_song():
    if request.method == "POST":
        song_name = request.form["song_name"]

        singer = request.form["singer"]

        album = request.form["album"]

        genre = request.form["genre"]

        duration = request.form["duration"]

        music_list[song_name] = {
            "singer": singer,
            "album": album,
            "genre": genre,
            "duration": duration,
            "favorite": False,
        }

        save_data()

        return redirect("/songs")

    return render_template("add_song.html")


# Update Song


@app.route("/update-song/<song_name>", methods=["GET", "POST"])
def update_song(song_name):
    if song_name in music_list:
        if request.method == "POST":
            singer = request.form["singer"]

            album = request.form["album"]

            genre = request.form["genre"]

            duration = request.form["duration"]

            music_list[song_name] = {
                "singer": singer,
                "album": album,
                "genre": genre,
                "duration": duration,
                "favorite": music_list[song_name]["favorite"],
            }

            save_data()

            return redirect("/songs")

        return render_template("update_song.html", song_name=song_name, details=music_list[song_name])

    return "Song Not Found"


# Delete Song


@app.route("/delete-song/<song_name>", methods=["POST"])
def delete_song(song_name):
    if song_name in music_list:
        del music_list[song_name]

        save_data()

    return redirect("/songs")


# Favorite Toggle


@app.route("/favorite-song/<song_name>")
def favorite_song(song_name):
    if song_name in music_list:
        current_status = music_list[song_name]["favorite"]

        music_list[song_name]["favorite"] = not current_status

        save_data()

    return redirect("/songs")


# Favorites Page


@app.route("/favorites")
def favorites():
    favorite_songs = {}

    for song, details in music_list.items():
        if details["favorite"]:
            favorite_songs[song] = details

    return render_template("favorites.html", favorite_songs=favorite_songs)


@app.route("/genres")
def genres():
    genres_data = {}

    for song, details in music_list.items():
        genre = details["genre"]

        if genre not in genres_data:
            genres_data[genre] = []

        genres_data[genre].append(song)

    return render_template("genres.html", genres_data=genres_data)


@app.route("/albums")
def albums():
    albums_data = {}

    for song, details in music_list.items():
        album = details["album"]

        if album not in albums_data:
            albums_data[album] = []

        albums_data[album].append(song)

    return render_template("albums.html", albums_data=albums_data)


if __name__ == "__main__":
    app.run(debug=True)
