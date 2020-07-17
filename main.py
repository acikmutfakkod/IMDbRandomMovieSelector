from imdb import IMDb
import random

class PickMovie():

    def __init__(self):
        self.top250 = IMDb().get_top250_movies()
        self.uid = 0
        self.random_movie()
        self.movie_info()

    def random_movie(self):
        id = random.randint(0, 249)
        print('{}: {}' .format(id, self.top250[id]))

        self.uid = IMDb().get_imdbID(self.top250[id])

    def movie_info(self):
        print(IMDb().get_movie_critic_reviews(self.uid))
        print(IMDb().get_movie_keywords(self.uid))
        print(IMDb().get_movie_release_dates(self.uid))

if __name__ == "__main__":
    PickMovie()
