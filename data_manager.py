import random
import itertools
import tmdbsimple as tmdb

tmdb.API_KEY = '3bd3415ab14ed2107bb5f34db8b8c587'  # TODO save to env. variable


def get_genres():
    genre = tmdb.Genres()
    movie_genres = genre.movie_list()['genres']
    tv_show_genres = genre.tv_list()['genres']
    return {"movie_genres": movie_genres, "tv_show_genres": tv_show_genres}


def fill_to_watch_list(is_movie):
    discover = tmdb.Discover()
    watch_list = []
    page = random.randint(1, 500)
    if (is_movie):
        watch_list.append(discover.movie(page=page, language='EN')['results'])
    else:
        watch_list.append(discover.tv(page=page, language='EN')['results'])

    watch_list = list(itertools.chain.from_iterable(watch_list))
    return watch_list


def get_random_movie(movieList):
    return random.choice(movieList)
