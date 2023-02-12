from movies import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False, unique=True)
    email = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password_text):
        self.password_hash = bcrypt.generate_password_hash(password_text).decode('utf-8')

    def check_password(self, attempted_password):
        if bcrypt.check_password_hash(self.password_hash, attempted_password):
            return True


class Actors(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False)
    origin = db.Column(db.String(length=20), nullable=False)
    birth_date = db.Column(db.Date(), nullable=False)

    # Objektum helyett névre hivatkozik
    def __repr__(self):
        return f'Actor {self.name}'


class MovieActors(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    movie_id = db.Column(db.Integer(), nullable=False)
    actor_id = db.Column(db.Integer(), nullable=False)


class Writers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False)
    origin = db.Column(db.String(length=20), nullable=False)

    # Objektum helyett névre hivatkozik
    def __repr__(self):
        return f'Writer {self.name}'


class Producers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False)
    origin = db.Column(db.String(length=20), nullable=False)

    # Objektum helyett névre hivatkozik
    def __repr__(self):
        return f'Producer {self.name}'


class Studios(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False)
    origin = db.Column(db.String(length=20), nullable=False)

    # Objektum helyett névre hivatkozik
    def __repr__(self):
        return f'Studio {self.name}'


class Genres(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False)

    # Objektum helyett névre hivatkozik
    def __repr__(self):
        return f'Genre {self.name}'


class MovieGenres(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    movie_id = db.Column(db.Integer(), nullable=False)
    genre_id = db.Column(db.Integer(), nullable=False)


class Movies(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False)
    logo = db.Column(db.VARCHAR(length=255), nullable=False)
    length = db.Column(db.Integer(), nullable=False)
    certificate = db.Column(db.Integer(), nullable=False)
    release_date = db.Column(db.Date(), nullable=False)
    writer_id = db.Column(db.Integer(), nullable=False)
    producer_id = db.Column(db.Integer(), nullable=False)
    studio_id = db.Column(db.Integer(), nullable=False)

    # Objektum helyett névre hivatkozik
