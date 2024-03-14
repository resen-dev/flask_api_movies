from flask import request, jsonify, Blueprint

from models.movie import Movie
from repositories.movie_repository import MovieRepository
from services.movie_service import MovieService

movies_bp = Blueprint('movies', __name__, url_prefix='/movies/v1')

movie_service = MovieService(MovieRepository())


@movies_bp.route('/', methods=['GET'])
def get_all_movies():
    try:
        return jsonify(movie_service.get_all_movies()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@movies_bp.route('/<int:id_movie>', methods=['GET'])
def get_movie_by_id(id_movie):
    try:
        return jsonify(movie_service.get_movie_by_id(id_movie)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@movies_bp.route('/<int:id_movie>', methods=['DELETE'])
def delete_movie_by_id(id_movie):
    try:
        movie_service.delete_movie_by_id(id_movie)
        return jsonify("Movie deleted!"), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@movies_bp.route('/', methods=['PUT'])
def update_movie():
    try:
        return jsonify(movie_service.update_movie(Movie(**request.json))), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@movies_bp.route('/', methods=['POST'])
def add_movie():
    try:
        return jsonify(movie_service.add_movie(Movie(**request.json))), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
