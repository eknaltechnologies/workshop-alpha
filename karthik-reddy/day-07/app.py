from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///music.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Song(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    mood = db.Column(db.String(50), nullable=False)
    poster = db.Column(db.String(500), nullable=False)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend_music():

    selected_mood = request.form.get("mood")
    recommended_songs = Song.query.filter_by(mood=selected_mood).all()

    return render_template("results.html", songs=recommended_songs, mood=selected_mood)


@app.route("/all-songs")
def all_songs():

    all_songs = Song.query.all()

    return render_template("results.html", songs=all_songs, mood="All Songs")


@app.route("/add-music", methods=["POST"])
def add_music():

    print(request.form)
    song_name = request.form.get("name")
    artist_name = request.form.get("artist")
    song_mood = request.form.get("mood")
    song_poster = request.form.get("poster")

    if not song_name or not artist_name or not song_mood:

        return "Please fill all required fields"

    new_song = Song(
        name=song_name,
        artist=artist_name,
        mood=song_mood,
        poster=song_poster,
    )
    db.session.add(new_song)
    db.session.commit()
    all_songs = Song.query.all()

    return render_template("results.html", songs=all_songs, mood="All Songs")


if __name__ == "__main__":

    with app.app_context():
        db.create_all()
    app.run(debug=True)
