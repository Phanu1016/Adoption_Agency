from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

def connect_database(app):
    """ Connect to database """
    database.app = app
    database.init_app(app)


class Pet(database.Model):
    """ Pet model for adoption """
    __tablename__ = 'pets'

    id = database.Column(database.Integer, nullable=False, primary_key=True, autoincrement=True)

    name = database.Column(database.Text, nullable=False)

    species = database.Column(database.Text, nullable=False)

    photo_url = database.Column(database.Text, nullable=True, default="https://i.ibb.co/qRpVdbn/noimage.png")

    age = database.Column(database.Integer, nullable=False, default=0)

    notes = database.Column(database.Text, nullable=True)

    available = database.Column(database.Boolean(45), nullable=False, default=True)
    


