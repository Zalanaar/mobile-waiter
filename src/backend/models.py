__all__ = ['Restaurants', 'Dishes', 'Compositions', 'Ingredients']

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    number_of_tables = db.Column(db.Integer, nullable=False)

    # У ресторана в меню много блюд (One-to-Many)
    dishes = db.relationship('Dishes', backref='restaurant', lazy=True)


class Dishes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    cost = db.Column(db.Integer, nullable=False)
    caloricity = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=False)

    # Каждое блюдо входит в меню одного ресторана (Many-to-One)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
