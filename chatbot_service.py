import requests
import utils
import urllib.parse
import time


api_url = "https://api.themoviedb.org/3"
movie_url = "/movie"
tv_show_url = "/tv"
language = "pt"

def get_tv_show_by_genre(genre):
    tv_show = []
    pagination_temp = 1
    pagination_control = True

    while pagination_control:
        movies_response = requests.get(api_url + f"/search{tv_show_url}query={urllib.parse.quote(genre)}&include_adult=true&language={language}&page={pagination_temp}", headers=utils.get_request_headers()).json()
        max_pages = movies_response['total_pages']

        if max_pages == pagination_temp:
            pagination_control = False

        # Controle da paginação
        if movies_response['total_pages'] != 1:
            pagination_temp += 1

        for movie in movies_response['results']:
            temp = {}

            temp['title'] = movie['title']
            temp['overview'] = movie['overview']
            temp['release_date'] = movie['release_date']

            tv_show.append(temp)

    return tv_show


def get_movies_by_genre(genre):
    movies = []
    pagination_temp = 1
    pagination_control = True

    while pagination_control:
        movies_response = requests.get(api_url + f"/search{movie_url}?query={urllib.parse.quote(genre)}&include_adult=true&language={language}&page={pagination_temp}", headers=utils.get_request_headers()).json()
        max_pages = movies_response['total_pages']

        if max_pages == pagination_temp:
            pagination_control = False

        # Controle da paginação
        if movies_response['total_pages'] != 1:
            pagination_temp += 1

        for movie in movies_response['results']:
            temp = {}

            temp['title'] = movie['title']
            temp['overview'] = movie['overview']
            temp['release_date'] = movie['release_date']

            movies.append(temp)

    return movies


def get_genres_array():
    genres = []

    genres_tmdb_response = get_genres(movie_url)

    for genre in genres_tmdb_response['genres']:
        genres.append(genre['name'])

    return genres


def get_genres(endpoint):
    genres = requests.get(api_url + f"/genre{endpoint}/list?language={language}", headers=utils.get_request_headers()).json()
    return genres
