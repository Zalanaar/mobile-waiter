from main import db
db.drop_all()
db.create_all()
from models import *


Mac = Restaurants(title='McDonalds', number_of_tables=30)
Burger = Dishes(title='Burger', cost=2, caloricity=500, weight=500, restaurant=Mac)

Cabbage = Ingredients(title='Cabbage')
Meat = Ingredients(title='Meat')

Burger.composition.append(Compositions(amount=200, ingredient=Cabbage))
Burger.composition.append(Compositions(amount=300, ingredient=Meat))

for item in [Mac, Burger, Cabbage, Meat]:
    db.session.add(item)
db.session.commit()

burger = Dishes.query.first()
print(burger.composition[1].ingredient.title)  # Meat


