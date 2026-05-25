from flask import Flask, request

app = Flask(__name__)

@app.route('/movies')
def movies_home():
    return '<h1> Hello Everyone! Welcome to my mini project movie list app📽️ </h1>'        


@app.route('/movies1/<movie_name>/<ott_platforms>')
def movie(movie_name, ott_platforms):
    return f'<h1> {movie_name} you can watch in {ott_platforms}. </h1>' 


@app.route('/movies2/<movie_name>/<int:release_year>')
def movie_year(movie_name, release_year):
    return f'<h1> {movie_name} was released in the year {release_year}. </h1>'


@app.route('/movies3/<movie_name>/<float:rating>')
def movie_rating(movie_name, rating):
    return f'<h1> {movie_name} has a rating of {rating} </h1>'


@app.route('/release_date/<movie_name>/<release_date>')
def movie_release_date(movie_name, release_date):
    return f'<b><h3>{movie_name} was released on {release_date}.</h3></b>'



@app.route('/director/<movie_name>/<director_name>')
def movie_director(movie_name, director_name):
    return f'<b><h3>{movie_name} is directed by {director_name}</h3></b>'



@app.route('/genre/<movie_name>/<genre>')
def movie_genre(movie_name, genre):
    return f'<b><h3>{movie_name} belongs to the {genre} genre.</h3></b>'



@app.route('/duration/<movie_name>/<int:duration>')
def movie_duration(movie_name, duration):
    return f'<b><h3>{movie_name} has a duration of {duration} minutes.</h3></b>'



@app.route('/language/<movie_name>/<language>')
def movie_language(movie_name, language):
    return f'<b><h3>{movie_name} is available in {language} language.</h3></b>'



@app.route('/budget/<movie_name>/<int:budget>')
def movie_budget(movie_name, budget):   
    return f'<b><h3>{movie_name} had a budget of {budget} crores.</h3></b>'



@app.route('/actors/<movie_name>/<actor>')
def movie_actors(movie_name, actor):
    return f'<b><h3>{movie_name} has a cast of {actor}.</h3></b>'



@app.route('/actress/<movie_name>/<actress>')   
def movie_actress(movie_name, actress):
    return f'<b><h3>{movie_name} has a leading actress {actress}.</h3></b>'



@app.route('/ratings')
def ratings():
    G = 'General Audiences'
    PG = 'Parental Guidance Suggested'
    PG_13 = 'Parents Strongly Cautioned'
    R = 'Restricted'
    NC_17 = 'Adults Only'
    return f'''
    <b>
    Movie Ratings:<br><br>
    G - {G}<br>
    PG - {PG}<br>
    PG-13 - {PG_13}<br>
    R - {R}<br>
    NC-17 - {NC_17}
    </b>
    '''



@app.route('/awards/<movie_name>/<awards>')
def movie_awards(movie_name, awards):
    return f'<b><h3>{movie_name} has won {awards} awards.</h3></b>'



@app.route('/franchise/<movie_name>/<franchise>')
def movie_franchise(movie_name, franchise):
    return f'<b><h3>{movie_name} is part of the {franchise} franchise.</h3></b>'




@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return '<h1> Welcome to the Movie List App! '
        'Explore various movies and their details 🎬 </h1>'
    else:
         return '<h1> Thank you for visiting! </h1>' 



@app.route('/add_movie', methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        return "<h1> Movie Added </h1>"
    else:
        return "<h1> No Updates </h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)

