import requests
import utils
import urllib.parse
import utils


def get_movies_or_tv_show_by_genre(genre, endpoint):
    movies_or_tv_show_array = []
    pagination_temp = 1
    pagination_control = True

    while pagination_control:
        response = requests.get(utils.api_url + f"/search{endpoint}?query={urllib.parse.quote(genre)}&include_adult=true&language={utils.language}&page={pagination_temp}", headers=utils.get_request_headers()).json()
        max_pages = response['total_pages']

        if max_pages == pagination_temp:
            pagination_control = False

        # Controle da paginação
        if response['total_pages'] != 1:
            pagination_temp += 1

        for movies_or_tv_show in response['results']:
            print(movies_or_tv_show)
            temp = {}

            if endpoint == "/movie":
                temp['title'] = movies_or_tv_show['title']
                temp['release_date'] = movies_or_tv_show['release_date']

            if endpoint == "/tv":
                temp['title'] = movies_or_tv_show['name']
                temp['release_date'] = movies_or_tv_show['first_air_date']

            temp['overview'] = movies_or_tv_show['overview']

            movies_or_tv_show_array.append(temp)

    return movies_or_tv_show_array


def get_genres_array():
    genres = []

    genres_tmdb_response = get_genres(utils.movie_url)

    for genre in genres_tmdb_response['genres']:
        genres.append(genre['name'])

    return genres


def get_genres(endpoint):
    genres = requests.get(utils.api_url + f"/genre{endpoint}/list?language={utils.language}", headers=utils.get_request_headers()).json()
    return genres
