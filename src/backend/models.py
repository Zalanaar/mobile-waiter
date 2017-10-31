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
    cost = db.Column(db.Integer, nullable=False)
    caloricity = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=False)

    # Каждое блюдо входит в меню одного ресторана (Many-to-One)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)

    composition = db.relationship("Compositions")


class Compositions(db.Model):
    dish_id = db.Column(db.Integer, db.ForeignKey('dishes.id'), primary_key=True)
    ingredient_id = db.Column(db.Text, db.ForeignKey('ingredients.title'), primary_key=True)

    amount = db.Column(db.Integer, nullable=False)

    ingredient = db.relationship('Ingredients')


class Ingredients(db.Model):
    title = db.Column(db.Text, primary_key=True)
