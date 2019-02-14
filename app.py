from flask import Flask, render_template, jsonify, request
import data_manager as dm

app = Flask(__name__)


@app.route('/')
def index():
    genres = dm.get_genres()
    return render_template('index.html', movie_genres=genres['movie_genres'], tv_show_genres=genres['tv_show_genres'])


@app.route('/get/movie', methods=['GET', 'POST'])
def get_movie():
    required_genre = request.form.to_dict()['id']
    print(required_genre)
    movies = dm.fill_to_watch_list(True, required_genre)
    movie = dm.get_random_movie(movies)
    names = dm.get_genre_name_by_id(movie['genre_ids'])
    movie['genre_names'] = names[:2]
    print(movie)
    return jsonify(movie)


@app.route('/get/tv', methods=['GET', 'POST'])
def get_show():
    shows = dm.fill_to_watch_list(False)
    show = dm.get_random_movie(shows)
    # fix different naming
    show['release_date'] = show.pop('first_air_date')
    show['title'] = show.pop('name')
    names = dm.get_genre_name_by_id(show['genre_ids'])
    show['genre_names'] = names[:2]
    return jsonify(show)


if __name__ == '__main__':
    app.run()
