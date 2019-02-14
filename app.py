from flask import Flask, render_template, jsonify
import random
import itertools
import tmdbsimple as tmdb

app = Flask(__name__)

tmdb.API_KEY = '3bd3415ab14ed2107bb5f34db8b8c587'   #TODO save to env. variable


@app.route('/')
def index():
    genre = tmdb.Genres()
    movie_genres = genre.movie_list()['genres']
    tv_show_genres = genre.tv_list()['genres']
    return render_template('index.html', movie_genres=movie_genres, tv_show_genres=tv_show_genres)


@app.route('/get/movie', methods=['GET', 'POST'])
def get_movie():
    movies = fill_to_watch_list(True)
    movie = get_random_movie(movies)
    return jsonify(movie)


@app.route('/get/tv', methods=['GET', 'POST'])
def get_show():
    shows = fill_to_watch_list(False)
    show = get_random_movie(shows)
    show['release_date'] = show.pop('first_air_date')
    show['title'] = show.pop('name')
    print(show)
    return jsonify(show)


def fill_to_watch_list(is_movie):
    discover = tmdb.Discover()
    watch_list = []
    page = random.randint(1, 500)
    if(is_movie):
        watch_list.append(discover.movie(page=page, language='EN')['results'])
    else:
        watch_list.append(discover.tv(page=page, language='EN')['results'])

    watch_list = list(itertools.chain.from_iterable(watch_list))
    return watch_list


def get_random_movie(movieList):
    return random.choice(movieList)


if __name__ == '__main__':
    app.run()
