from dao.model.movie import Movie

class MovieDAO:

    def __init__(self, session):
        self.session = session
        self.model = Movie


    def get_all(self, filters):
        if filters['director_id']:
            return self.session.query(self.model).filter(self.model.director_id == filters['director_id']).all()
        elif filters['genre_id']:
            return self.session.query(self.model).filter(self.model.genre_id == filters['genre_id']).all()
        elif filters['year_id']:
            return self.session.query(self.model).filter(self.model.year_id == filters['year_id']).all()

        return self.session.query(self.model).all()

    def get_by_id(self, mid):
        return self.session.query(self.model).get(mid)


    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie


    def update(self, data):
        movie = self.get_by_id(data['id'])
        movie.name = data['name']

        self.session.add(movie)
        self.session.commit()


    def delete(self, mid):
        movie = self.get_by_id(mid)
        self.session.delete(movie)
        self.session.commit()
