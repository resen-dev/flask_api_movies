from abc import ABC, abstractmethod
from typing import List

from models.movie import Movie


class MovieServiceInterface(ABC):

    @abstractmethod
    def get_all_movies(self) -> List[Movie]:
        raise Exception("Not implemented")

    @abstractmethod
    def get_movie_by_id(self, id_movie: int) -> Movie:
        raise Exception("Not implemented")

    @abstractmethod
    def delete_movie_by_id(self, updated_movie: int) -> None:
        raise Exception("Not implemented")

    @abstractmethod
    def update_movie(self, movie: Movie) -> Movie:
        raise Exception("Not implemented")

    def add_movie(self, movie: Movie) -> Movie:
        raise Exception("Not implemented")
