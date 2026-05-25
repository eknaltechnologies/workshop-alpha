from flask import Flask, request

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return """
    <h1>🎵 Music App</h1>

    <h3>Try These URLs:</h3>

    <ul>
        <li>/music/Believer</li>
        <li>/singer/Believer/ImagineDragons</li>
        <li>/likes/Believer/5000000</li>
        <li>/genre/Believer/Rock</li>
        <li>/duration/Believer/4</li>
        <li>/album/Believer/Evolve</li>
        <li>/language/Believer/English</li>
        <li>/rating/Believer/4.9</li>
        <li>/release/Believer/2017</li>
    </ul>

    <hr>

    <h2>Add Music Details</h2>

    <form action="/submit" method="POST">

        <input type="text" name="music" placeholder="Music Name"><br><br>

        <input type="text" name="singer" placeholder="Singer Name"><br><br>

        <input type="text" name="genre" placeholder="Genre"><br><br>

        <button type="submit">Submit</button>

    </form>
    """


@app.route("/music/<music_name>")
def music(music_name):
    return f"<h1>🎶 Music Name: {music_name}</h1>"


@app.route("/singer/<music_name>/<singer_name>")
def singer(music_name, singer_name):
    return f"<h2>{music_name} is sung by {singer_name}</h2>"


@app.route("/likes/<music_name>/<int:likes>")
def likes(music_name, likes):
    return f"<h2>{music_name} has {likes} likes 👍</h2>"


@app.route("/genre/<music_name>/<genre>")
def genre(music_name, genre):
    return f"<h2>{music_name} belongs to {genre} genre 🎸</h2>"


@app.route("/duration/<music_name>/<int:minutes>")
def duration(music_name, minutes):
    return f"<h2>{music_name} duration is {minutes} minutes ⏱️</h2>"


@app.route("/album/<music_name>/<album_name>")
def album(music_name, album_name):
    return f"<h2>{music_name} is from {album_name} album 💿</h2>"


@app.route("/language/<music_name>/<language>")
def language(music_name, language):
    return f"<h2>{music_name} is available in {language} language 🌍</h2>"


@app.route("/rating/<music_name>/<float:rating>")
def rating(music_name, rating):
    return f"<h2>{music_name} rating is {rating} ⭐</h2>"


@app.route("/release/<music_name>/<int:year>")
def release(music_name, year):
    return f"<h2>{music_name} was released in {year} 📅</h2>"


@app.route("/submit", methods=["POST"])
def submit():

    music_name = request.form["music"]
    singer_name = request.form["singer"]
    genre_name = request.form["genre"]

    return f"""

    <h1>🎵 Music Details Submitted</h1>

    <h2>Music Name : {music_name}</h2>

    <h2>Singer Name : {singer_name}</h2>

    <h2>Genre : {genre_name}</h2>

    """


if __name__ == "__main__":
    app.run(debug=True)
