import random
import itertools
import tmdbsimple as tmdb

tmdb.API_KEY = '3bd3415ab14ed2107bb5f34db8b8c587'  # TODO save to env. variable


def get_genres():
    genre = tmdb.Genres()
    movie_genres = genre.movie_list()['genres']
    tv_show_genres = genre.tv_list()['genres']
    return {"movie_genres": movie_genres, "tv_show_genres": tv_show_genres}


def fill_to_watch_list(is_movie, required_genre):
    discover = tmdb.Discover()
    watch_list = []
    if is_movie:
        if required_genre != "0":
            page = random.randint(1, 200)
            watch_list.append(discover.movie(page=page, language='EN', with_genres=required_genre)['results'])
        else:
            page = random.randint(1, 500)
            watch_list.append(discover.movie(page=page, language='EN')['results'])
    else:
        if required_genre != "0":
            page = random.randint(1, 100)
            watch_list.append(discover.tv(page=page, language='EN', with_genres=required_genre)['results'])
        else:
            page = random.randint(1, 500)
            watch_list.append(discover.tv(page=page, language='EN')['results'])
    watch_list = list(itertools.chain.from_iterable(watch_list))

    return watch_list


def get_random_movie(movieList):
    return random.choice(movieList)


def get_genre_name_by_id(genre_ids):
    all_genres = merge_movie_tv_genres()
    genre_names = []
    for genre in all_genres:
        if genre['id'] in genre_ids:
            genre_names.append(genre['name'])
    return genre_names


def merge_movie_tv_genres():
    genre = tmdb.Genres()
    movie_genres = genre.movie_list()['genres']
    tv_show_genres = genre.tv_list()['genres']
    return list({x['id']: x for x in movie_genres + tv_show_genres}.values())
