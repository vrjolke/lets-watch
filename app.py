from flask import Flask, render_template, jsonify
import random
import itertools
import tmdbsimple as tmdb

app = Flask(__name__)

tmdb.API_KEY = '3bd3415ab14ed2107bb5f34db8b8c587'   #TODO save to env. variable


@app.route('/')
def hello_world():
    genre = tmdb.Genres()
    genres = genre.movie_list()['genres']
    return render_template('index.html', genres=genres)


@app.route('/get/movie')
def api_test():
    # pp = pprint.PrettyPrinter(indent=4)
    movies = fill_movie_list(5)
    movie = get_random_movie(movies)
    return jsonify(movie)


def fill_movie_list(pageCount):
    discover = tmdb.Discover()
    movies = []
    for i in range(pageCount):
        movies.append(discover.movie(page=i + 1)['results'])
    movies = list(itertools.chain.from_iterable(movies))

    return movies


def get_random_movie(movieList):
    return random.choice(movieList)


if __name__ == '__main__':
    app.run()
