from abc import ABC, abstractclassmethod, abstractmethod
from typing import List, Optional

from models.movie import Movie


class MovieRepositoryInterface(ABC):
    @abstractmethod
    def get_all_movies(self) -> List[Movie]:
        raise Exception("Not implemented")

    @abstractmethod
    def get_movie_by_id(self, id_movie: int) -> Optional[Movie]:
        raise Exception("Not implemented")

    @abstractmethod
    def delete_movie_by_id(self, id_movie: int) -> None:
        raise Exception("Not implemented")

    @abstractmethod
    def update_movie(self, updated_movie: Movie) -> Optional[Movie]:
        raise Exception("Not implemented")

    @abstractmethod
    def add_movie(self, movie: Movie) -> Movie:
        raise Exception("Not implemented")
