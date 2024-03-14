from typing import List, Optional
from models.movie import Movie
from interfaces.movie_repository_interface import MovieRepositoryInterface


class MovieRepository(MovieRepositoryInterface):
    def __init__(self):
        self._movies: List[Movie] = []

    def increment_id(self) -> int:
        if self._movies:
            return max(movie.id for movie in self._movies) + 1
        return 1

    def get_all_movies(self) -> List[Movie]:
        return self._movies

    def get_movie_by_id(self, id_movie: int) -> Optional[Movie]:
        for movie in self._movies:
            if movie.id == id_movie:
                return movie
        return None

    def delete_movie_by_id(self, id_movie: int) -> None:
        movie = self.get_movie_by_id(id_movie)

        if not movie:
            raise ValueError(f"Movie with id {id_movie} don't exists")

        self._movies.remove(movie)

    def update_movie(self, updated_movie: Movie) -> Optional[Movie]:
        old_movie = self.get_movie_by_id(updated_movie.id)

        if not old_movie:
            raise ValueError(f"Movie with id {updated_movie.id} don't exists")

        self._movies[self._movies.index(old_movie)] = updated_movie
        return updated_movie

    def add_movie(self, movie: Movie) -> Movie:
        movie.id = self.increment_id()
        self._movies.append(movie)
        return movie
