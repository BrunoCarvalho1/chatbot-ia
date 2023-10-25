import chatbot_service
import utils


def main():
    movies_or_tv_show = chatbot_service.get_movies_or_tv_show_by_genre('Ação', utils.tv_show_url)
    for movie_or_tv_show in movies_or_tv_show:
        print(movie_or_tv_show)


if __name__ == "__main__":
    main()
