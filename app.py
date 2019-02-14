from flask import Flask, render_template, jsonify
import data_manager as dm

app = Flask(__name__)


@app.route('/')
def index():
    genres = dm.get_genres();
    return render_template('index.html', movie_genres=genres['movie_genres'], tv_show_genres=genres['tv_show_genres'])


@app.route('/get/movie', methods=['GET', 'POST'])
def get_movie():
    movies = dm.fill_to_watch_list(True)
    movie = dm.get_random_movie(movies)
    return jsonify(movie)


@app.route('/get/tv', methods=['GET', 'POST'])
def get_show():
    shows = dm.fill_to_watch_list(False)
    show = dm.get_random_movie(shows)
    show['release_date'] = show.pop('first_air_date')
    show['title'] = show.pop('name')
    print(show)
    return jsonify(show)




if __name__ == '__main__':
    app.run()
