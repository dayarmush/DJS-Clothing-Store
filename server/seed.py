from models.favorites import Favorite
from models.items import Item
from models.reviews import Review
from models.shopping_cart import ShoppingCart
from models.user import User
from config import db
from app import app
from faker import Faker
from random import choice as rc, randint

fake = Faker()

# Add User id
def create_favorites():
    faves = []
    for i in range(30):
        fave = Favorite(
            user_id=randint(1, 30)
        )
        faves.append(fave)
    return [fave.id for fave in faves], faves

# add Cart id and Favorite id
def create_items():
    categories =  ["Men's", "Women's", 'kids']
    clothing_items = [
        "T-shirt",
        "Jeans",
        "Dress",
        "Sweater",
        "Hoodie",
        "Shorts",
        "Skirt",
        "Blouse",
        "Blazer",
        "Suit",
        "Coat",
        "Jacket",
        "Vest",
        "Tank top",
        "Cardigan",
        "Jumpsuit",
        "Romper",
        "Polo shirt",
        "Sweatshirt",
        "Leggings",
        "Cargo pants",
        "Capri pants",
        "Overalls",
        "Pajamas",
        "Bathrobe",
        "Onesie",
        "Trench coat",
        "Peacoat",
        "Kimono",
        "Sarong",
        "Maxi dress",
        "Mini skirt",
        "Midi dress",
        "Crop top",
        "Chinos",
        "Flannel shirt",
        "Camisole",
        "Halter top",
        "Poncho",
        "Shawl",
        "Kaftan",
        "Anorak",
        "Windbreaker",
        "Raincoat",
        "Parka",
        "Turtleneck",
        "Polo dress",
        "Sun dress",
        "Tuxedo",
        "Tuxedo dress",
        "Ruffled blouse",
        "Pencil skirt",
        "A-line skirt",
        "Culottes",
        "Cargo shorts",
        "Athletic shorts",
        "Denim jacket",
        "Leather jacket",
        "Suede jacket",
        "Down jacket",
        "Kimono jacket",
        "Off-the-shoulder top",
        "Button-up shirt",
        "Puffer coat",
        "Sheath dress",
        "Jeggings",
        "Harem pants",
        "Capris",
        "Cap sleeve top",
        "Bell-bottoms",
        "Jumper dress",
        "Bandeau top",
        "Fishnet stockings",
        "Pashmina scarf",
        "Ascot tie",
        "Headband",
        "Leg warmers",
        "Newsboy cap",
        "Beret",
        "Bow tie",
        "Necktie",
        "Pocket square",
        "Cravat",
        "Bowler hat",
        "Beanie",
        "Fedora",
        "Visor",
        "Snapback cap",
        "Boater hat",
        "Newsboy cap",
        "Trench dress",
        "Tunic dress",
        "Cold shoulder top",
        "Ringer T-shirt",
        "Joggers",
        "Biker jacket",
        "Chore coat",
        "Peplum top",
        "Tulle skirt",
        "Palazzo pants"
    ]
    items = []
    for i in range(100):
        item = Item(
            name=rc(clothing_items),
            image=fake.file_extension(category='image'),
            price=randint(1, 100),
            category=rc(categories),
            cart_id = randint(1, 10),
            favorite_id=randint(1, 30)
        )
        items.append(item)
    return [item.id for item in items], items

# Add Item id and User id 
def create_reviews():
    reviews = []
    for i in range(90):
        review = Review(
            text=fake.sentence(),
            rating=randint(0, 5),
            user_id=randint(1, 30),
            item_id=randint(1, 100)
        )
        reviews.append(review)
    return [review.id for review in reviews], reviews

# Add User id 
def create_carts():
    carts = []
    for i in range(10):
        cart = ShoppingCart(
            user_id=randint(1, 30)
        )
        carts.append(cart)
    return [cart.id for cart in carts], carts

def create_users():
    users = []
    for i in range(30):
        user = User(
            username=fake.name(),
        )
        user.password_hash = fake.last_name()
        users.append(user)
    return [user.id for user in users], users

if __name__ == '__main__':
    with app.app_context():
        print('Clearing db...')
        User.query.delete()
        ShoppingCart.query.delete()
        Review.query.delete()
        Item.query.delete()
        Favorite.query.delete()

        print('seeding db...')
        users_id, users = create_users()
        carts_id, carts = create_carts()
        faves_id, favorites = create_favorites()
        items_id, items = create_items()
        reviews_id, reviews = create_reviews()

        # Might need to be in parens
        print('adding to db...')
        db.session.add_all(users)
        db.session.add_all(carts)
        db.session.add_all(favorites)
        db.session.add_all(items)
        db.session.add_all(reviews)
        db.session.commit()

