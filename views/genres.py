from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenreView(Resource):

    def get(self):
        genres = genre_service.get_all()
        result = GenreSchema(many=True).dump(genres)
        return result, 200



@genres_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):
        genre = genre_service.get_one(gid)
        result = GenreSchema().dump(genre)
        return result, 200

