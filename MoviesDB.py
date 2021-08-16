import random

import Movie
from tinydb import TinyDB, Query


class MoviesDBWrapper:
    DB_PATH: str = 'movies_data_base.json'
    DB: TinyDB = TinyDB(DB_PATH)

    @classmethod
    def movies_by_genre(cls, genres: list, limit: int = 10) -> list[Movie.Movie]:
        item = Query()
        movies = MoviesDBWrapper.DB.search(item.genres.all(genres))
        if len(movies) > limit:
            index = random.randrange(0,len(movies) - limit)
            movies = movies[index:index + limit]
        result = []
        for movie in movies:
            result.append(MoviesDBWrapper.__to_movie(movie))
        return result

    @classmethod
    def top_n_movies(cls, n: int = 10) -> list[Movie.Movie]:
        return MoviesDBWrapper.movies_by_genre([])[:n]

    @classmethod
    def movies_by_situations(cls, situation: str) -> list[Movie.Movie]:
        if situation == "Friends":
            return MoviesDBWrapper.movies_by_genre(['Comedy', 'Action'])
        if situation == "Family":
            return MoviesDBWrapper.movies_by_genre(['Animation', 'Family', 'Adventure'])
        if situation == "Date":
            return MoviesDBWrapper.movies_by_genre(["Romance"])
        if situation == "Myself & I":
            return MoviesDBWrapper.movies_by_genre([])


    @classmethod
    def insert(cls, movie: Movie.Movie):
        MoviesDBWrapper.DB.insert({'title': movie.title, 'rating': movie.rating, 'genres': movie.genres})

    @classmethod
    def __to_movie(cls, data: dict) -> Movie.Movie:
        return Movie.Movie(data["title"], data["rating"], data["genres"])



print(MoviesDBWrapper.movies_by_genre([]))