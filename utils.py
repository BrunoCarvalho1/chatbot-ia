import os


api_url = "https://api.themoviedb.org/3"
language = "pt"
movie_url = "/movie"
tv_show_url = "/tv"

def get_api_key():
    return os.environ['TMDB_API_KEY']


def get_request_headers():
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + get_api_key()
    }

    return headers

