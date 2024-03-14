from typing import List, Optional, Type
from models.movie import Movie

from interfaces.movie_repository_interface import MovieRepositoryInterface
from interfaces.movie_service_interface import MovieServiceInterface


class MovieService(MovieServiceInterface):
    def __init__(self, movie_repository: MovieRepositoryInterface):
        self.movie_repository = movie_repository

    def get_all_movies(self) -> List[Movie]:
        return self.movie_repository.get_all_movies()

    def get_movie_by_id(self, id_movie: int) -> Optional[Movie]:

        movie = self.movie_repository.get_movie_by_id(id_movie)

        return movie if movie else "Movie not found"

    def delete_movie_by_id(self, id_movie: int) -> None:
        self.movie_repository.delete_movie_by_id(id_movie)

    def update_movie(self, updated_movie: Movie) -> Optional[Movie]:
        return self.movie_repository.update_movie(updated_movie)

    def add_movie(self, movie: Movie) -> Movie:
        return self.movie_repository.add_movie(movie)
