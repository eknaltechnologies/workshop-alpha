from flask import Flask, redirect, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 1. Initialization and App Configuration
app = Flask(__name__)

# Clean shortcut path configuration matching your workshop session photo exactly
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 2. Database and Migration Engine Binding
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# 3. Database ORM Model Definitions
class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    mood = db.Column(db.String(50), nullable=False)
    emoji = db.Column(db.String(10), nullable=False)
    poster = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Movie {self.name}>"


# 4. Pure Python Data Seeding Core Logic
def seed_database_directly():
    """Populates the database with default entries on first load if it is completely empty."""
    if Movie.query.count() == 0:
        default_telugu_movies = [
            {
                "name": "Ee Nagaraniki Emaindi",
                "genre": "Comedy/Drama",
                "mood": "Happy",
                "emoji": "🍻",
                "poster": "https://m.media-amazon.com/images/M/MV5BM2FmOGE3MzYtYTljMy00Njk4LWI5YWYtM2M2OTIwMGEzZWE1XkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Jersey",
                "genre": "Sports/Drama",
                "mood": "Sad",
                "emoji": "🏏",
                "poster": "https://upload.wikimedia.org/wikipedia/en/2/2a/Jersey_2022_poster.jpg",
            },
            {
                "name": "RRR",
                "genre": "Action/Drama",
                "mood": "Excited",
                "emoji": "🐅",
                "poster": "https://m.media-amazon.com/images/M/MV5BNWMwODYyMjQtMTczMi00NTQ1LWFkYjItMGJhMWRkY2E3NDAyXkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Fidaa",
                "genre": "Romance/Drama",
                "mood": "Relaxed",
                "emoji": "🌾",
                "poster": "https://m.media-amazon.com/images/M/MV5BODg5MmYwMDEtN2Q2NC00Njg3LWFlZDEtN2FlYTE0YTU0NDFmXkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Jatha Kalise",
                "genre": "Romance/Comedy",
                "mood": "Romantic",
                "emoji": "💞",
                "poster": "https://m.media-amazon.com/images/S/pv-target-images/42b3395680e0bbaa95824441612f65d67e606f98dc51a9ce64eb1fdbeae76227.jpg",
            },
            {
                "name": "Pushpa: The Rise",
                "genre": "Action/Crime",
                "mood": "Excited",
                "emoji": "🪓",
                "poster": "https://m.media-amazon.com/images/S/pv-target-images/2844b9fb2959bff43271a6ce5fb2519c16aef711885b08f71b6c1cbffb060ee7.jpg",
            },
            {
                "name": "Baahubali: The Beginning",
                "genre": "Fantasy/Action",
                "mood": "Adventurous",
                "emoji": "⚔️",
                "poster": "https://m.media-amazon.com/images/M/MV5BM2YxZThhZmEtYzM0Yi00OWYxLWI4NGYtM2Y2ZDNmOGE0ZWQzXkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Mahanati",
                "genre": "Biography/Drama",
                "mood": "Melancholic",
                "emoji": "🎥",
                "poster": "https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/mahanati-et00054544-09-03-2017-05-04-00.jpg",
            },
            {
                "name": "Masooda",
                "genre": "Horror/Thriller",
                "mood": "Fearful",
                "emoji": "👻",
                "poster": "https://static.filmyfocus.com/wp-content/uploads/2022/11/Masooda-Movie-Review-and-Rating2.jpg",
            },
            {
                "name": "Pelli Choopulu",
                "genre": "Romance/Comedy",
                "mood": "Happy",
                "emoji": "🍳",
                "poster": "https://indianmoviesblog.wordpress.com/wp-content/uploads/2021/04/image.jpg",
            },
            {
                "name": "Ninnu Kori",
                "genre": "Romance/Drama",
                "mood": "Sad",
                "emoji": "🌧️",
                "poster": "https://m.media-amazon.com/images/S/pv-target-images/f4aa623d9fb26421fec29f384e8fbb43bb100364ca32cbe6e85f46ab9958c8bc.jpg",
            },
            {
                "name": "Agent Sai Srinivasa Athreya",
                "genre": "Comedy/Thriller",
                "mood": "Excited",
                "emoji": "🔍",
                "poster": "https://m.media-amazon.com/images/M/MV5BZDRiMjY1ZjQtNzFkNC00NmVhLWIyZTQtNTAzMGUzMTMxMzdkXkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "C/o Kancharapalem",
                "genre": "Anthology/Drama",
                "mood": "Calm",
                "emoji": "🏡",
                "poster": "https://upload.wikimedia.org/wikipedia/en/d/d3/C-o_Kancharapalem.jpg",
            },
            {
                "name": "Geetha Govindam",
                "genre": "Romance/Comedy",
                "mood": "Happy",
                "emoji": "🚌",
                "poster": "https://m.media-amazon.com/images/M/MV5BNWI3OTcwN2EtMDQ2MS00YTQ2LTliZDEtYTM4YTIzNDU5ODMyXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            },
            {
                "name": "Sita Ramam",
                "genre": "Romance/Drama",
                "mood": "Romantic",
                "emoji": "✉️",
                "poster": "https://upload.wikimedia.org/wikipedia/en/1/1d/Sita_Ramam.jpg",
            },
            {
                "name": "Karthikeya 2",
                "genre": "Mystery/Adventure",
                "mood": "Adventurous",
                "emoji": "🦚",
                "poster": "https://m.media-amazon.com/images/M/MV5BZmYwMjhjY2QtYjZiMC00ZmQ0LTkyMzAtYjM2YTU0OWI4NTBhXkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Hi Nanna",
                "genre": "Family/Drama",
                "mood": "Sad",
                "emoji": "👨‍👧",
                "poster": "https://m.media-amazon.com/images/M/MV5BNDVhNjJkYTItZDUyMS00NDc3LWI4YzctNzc4YWUyYjRkZmVlXkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "DJ Tillu",
                "genre": "Comedy/Crime",
                "mood": "Energetic",
                "emoji": "🎧",
                "poster": "https://m.media-amazon.com/images/M/MV5BYjlhZmIzMDUtODk1MS00N2Y4LThkYzUtNDQ0NmQwM2U0MmY3XkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Eega",
                "genre": "Fantasy/Action",
                "mood": "Excited",
                "emoji": "🪰",
                "poster": "https://m.media-amazon.com/images/M/MV5BMTA0MDFmMDMtMTE5OC00YWQ0LWIwZTUtOWIwMjk4Yjc3NGY1XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            },
            {
                "name": "Anand",
                "genre": "Romance/Drama",
                "mood": "Relaxed",
                "emoji": "☕",
                "poster": "https://m.media-amazon.com/images/M/MV5BNDQ3Y2RlOTgtNTFmMy00NmM0LWFmNzYtOTI5OTNhYmM2NmJmXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            },
            {
                "name": "Virupaksha",
                "genre": "Mystery/Horror",
                "mood": "Scared",
                "emoji": "🦅",
                "poster": "https://m.media-amazon.com/images/M/MV5BZjZmNDVhNTUtMzE0Zi00ZWZjLTllZjAtY2Q3MGQ1NDU0ZDhiXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            },
            {
                "name": "Brochevarevarura",
                "genre": "Comedy/Crime",
                "mood": "Happy",
                "emoji": "🎬",
                "poster": "https://m.media-amazon.com/images/M/MV5BMDAxNWNmNGEtYTJhYi00NTdjLWExZDgtZWYyM2FhODdmMzBmXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            },
            {
                "name": "Majili",
                "genre": "Romance/Drama",
                "mood": "Melancholic",
                "emoji": "🌧️",
                "poster": "https://m.media-amazon.com/images/M/MV5BZjNhMmI4NzUtMjUyOC00OGU5LThhNDAtZGMwMTIwMjc1OTRkXkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Goodachari",
                "genre": "Action/Spy",
                "mood": "Excited",
                "emoji": "🕶️",
                "poster": "https://m.media-amazon.com/images/M/MV5BZTRmZDQyMzctMzA2Zi00YWEzLTg1MTUtOTdhNTMyMzJiN2M5XkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Sammohanam",
                "genre": "Romance/Drama",
                "mood": "Relaxed",
                "emoji": "🎨",
                "poster": "https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/sammohanam-et00071484-23-02-2018-02-18-29.jpg",
            },
            {
                "name": "Gamyam",
                "genre": "Road/Drama",
                "mood": "Calm",
                "emoji": "🏍️",
                "poster": "https://m.media-amazon.com/images/M/MV5BNDljNGFmNTQtZjlkZS00ZWIyLWE1ZWQtODQ2YzI3NGNhNDkxXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            },
            {
                "name": "Mathu Vadalara",
                "genre": "Comedy/Thriller",
                "mood": "Happy",
                "emoji": "💊",
                "poster": "https://m.media-amazon.com/images/M/MV5BZTU4ZWRlYTUtNGY0Yy00NDNjLThlNzQtY2M1NDNiOWM5MWJkXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            },
            {
                "name": "Arjun Reddy",
                "genre": "Romance/Drama",
                "mood": "Angry",
                "emoji": "🕶️",
                "poster": "https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Arjun_Reddy.jpg/250px-Arjun_Reddy.jpg",
            },
            {
                "name": "Vikram",
                "genre": "Action/Thriller",
                "mood": "Excited",
                "emoji": "🚗",
                "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQDfkDWR2xTZDcmDdOp7kJQHO6aqQr1e3BjQ&s",
            },
            {
                "name": "Sye Raa Narasimha Reddy",
                "genre": "Historical/Action",
                "mood": "Adventurous",
                "emoji": "🛡️",
                "poster": "https://m.media-amazon.com/images/M/MV5BNzMxMTc1MDAtOWNkNy00NDc4LThmZWQtZGJiOWM5ODdhMWI2XkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Mallesham",
                "genre": "Biography/Drama",
                "mood": "Inspirational",
                "emoji": "🧵",
                "poster": "https://m.media-amazon.com/images/M/MV5BMWFmOWJhZGMtNzZlZS00ODE5LWFhMjUtOTc4OTAxY2ZmZTZjXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            },
            {
                "name": "Sarkaru Vaari Paata",
                "genre": "Action/Comedy",
                "mood": "Energetic",
                "emoji": "💰",
                "poster": "https://m.media-amazon.com/images/M/MV5BYjI0M2Q5MzgtNzBkZi00ZGE4LTgxZGEtYTk2NWI2NmY3MDZhXkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Oopiri",
                "genre": "Comedy/Drama",
                "mood": "Hopeful",
                "emoji": "👊",
                "poster": "https://m.media-amazon.com/images/M/MV5BNte5NmM5YWQtNWYyYi00OWE5LTg3ZmItYmVjMDc3OTJiOTBlXkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "K.G.F: Chapter 1",
                "genre": "Action/Thriller",
                "mood": "Adventurous",
                "emoji": "⛏️",
                "poster": "https://m.media-amazon.com/images/M/MV5BNDVlYWYzNDUtZTM3Ny00OTI5LThiZDQtNTA0YjFhMTE1YTdjXkEyXkFqcGc@._V1_.jpg",
            },
            {
                "name": "Vakeel Saab",
                "genre": "Legal/Drama",
                "mood": "Serious",
                "emoji": "⚖️",
                "poster": "https://m.media-amazon.com/images/M/MV5BYWM0Y2YyMmYtYjhjYS00NTc2LTllZjktZDMxMWFkMGFmMzU2XkEyXkFqcGc@._V1_.jpg",
            },
        ]

        try:
            for m in default_telugu_movies:
                movie_record = Movie(
                    name=m["name"],
                    genre=m["genre"],
                    mood=m["mood"],
                    emoji=m["emoji"],
                    poster=m["poster"],
                )
                db.session.add(movie_record)
            db.session.commit()
            print("🎉 Database successfully seeded with movie elements!")
        except Exception as e:
            print(f"⚠️ Error occurred while seeding database: {e}")


# 5. Routing Controllers
@app.route("/")
def home():
    seed_database_directly()
    return render_template("home.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    selected_mood = request.form.get("mood")
    result = Movie.query.filter(Movie.mood.ilike(selected_mood)).all()
    return render_template("result.html", movies=result, mood=selected_mood)


@app.route("/add-movie", methods=["POST"])
def add_movie():
    new_movie = Movie(
        name=request.form.get("name"),
        genre=request.form.get("genre"),
        mood=request.form.get("mood"),
        emoji=request.form.get("emoji"),
        poster=request.form.get("poster"),
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
