import imdb
import MoviesDB
import Movie


class ImdbConnectorWrapper:
    """Class ImdbConnectorWrapper represent the responsibility to connect with IDMb"""

    @classmethod
    def get_imdb_data_base(cls):
        """
        This function returns list of 250 top movies from IDMb's data base
        :return: a list of Movie objects witch contains title, rating and genres.
        """
        ia = imdb.IMDb()
        top250 = ia.get_top250_movies()
        for movie_count in range(0, 250):
            movie_object = ia.get_movie(top250[movie_count].movieID)
            title = movie_object['title']
            rating = movie_object['rating']
            genres = movie_object['genres']
            movie = Movie.Movie(title, rating, genres)
            MoviesDB.MoviesDBWrapper.insert(movie)


# create the data base
ImdbConnectorWrapper.get_imdb_data_base()
