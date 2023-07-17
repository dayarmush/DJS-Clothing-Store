from models.favorites import Favorite
from models.items import Item
from models.reviews import Review
from models.shopping_cart import ShoppingCart
from models.user import User
from .config import db
from app import app
from faker import Faker
from random import choice as rc, randint

fake = Faker()

# Add User id
def create_favorites(users):
    faves = []
    for i in range(50):
        fave = Favorite(
            user_id=rc(users)
        )
        faves.append(fave)
    return faves

# add Cart id and Favorite id
def create_items(carts, favorites):
    items = []
    for i in range(50):
        item = Item(
            name=fake.commerce.product(),
            image=fake.image.fashion(),
            price=randint(0, 100),
            cart_id = rc(carts),
            favorites=rc(favorites)
        )
        items.append(item)
    return items

# Add Item id and User id 
def create_reviews(users, items):
    reviews = []
    for i in range(50):
        review = Review(
            text=fake.lorem.sentence(),
            rating=randint(0, 5),
            user_id=rc(users),
            item_id=rc(items)
        )
        reviews.append(review)
    return reviews

# Add User id 
def create_carts(users):
    carts = []
    for i in range(50):
        cart = ShoppingCart(
            user_id=rc(users)
        )
        carts.append(cart)
    return carts

def create_users():
    users = []
    for i in range(50):
        user = User(
            username=fake.name.firstName(),
        )
        user.password_hash = fake.name.lastName()
        users.append(user)
    return users

if __name__ == '__main__':
    with app.app_context():
        print('Clearing db...')
        User.query.delete()
        ShoppingCart.query.delete()
        Review.query.delete()
        Item.query.delete()
        Favorite.query.delete()

        print('seeding db...')
        users = create_users()
        carts = create_carts(users)
        favorites = create_favorites(users)
        items = create_items(carts, favorites)
        reviews = create_reviews(users, items)

        # Might need to be in parens
        print('adding to db...')
        db.session.add_all(users, carts, favorites, items, reviews)
        db.session.commit()

