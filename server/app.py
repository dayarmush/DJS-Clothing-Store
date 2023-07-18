from models.favorites import Favorite
from models.items import Item
from models.reviews import Review
from models.shopping_cart import ShoppingCart
from models.user import User
from .config import Flask, Migrate, db, request, session
import os

# Create Flask Instance
app = Flask(__name__)

# Set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

# Set the secret key for cookie session
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Disables db tracking can improve performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Change to true when in production
app.json.compact = False

migrate = Migrate(app, db)

# Connecting the flask app to sqlalchemy/db
db.init_app(app)

# Routes
@app.post('/signup')
def post_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return {'error': 'you need username and password'}, 400

    user = User.query.filter_by(username=username).first()

    if user:
        return {'error': 'Username already exists'}, 400

    try:
        user = User(
            username=username
        )

        user.password_hash(password)

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id
        session['is_admin'] = user.admin

        return user.to_dict(), 201
    except:
        return {'error': 'Signup failed'}, 400
    
@app.post('/carts')
def add_cart():
    data = request.get_json()

    try:
        cart = ShoppingCart(
            user_id=data.get('user_id')
        )

        db.session.add(cart)
        db.session.commit()

        return cart.to_dict(), 201
    
    except:
        return {'error': 'Add to cart failed'}, 400

@app.delete('/carts/<int:id>')
def delete_cart(id):

    cart = ShoppingCart.query.filter_by(id=id).first()

    if not cart:
        return {'error': 'cart not found'}
    
    db.session.delete(cart)
    db.session.commit()

    return {}, 200

@app.post('/reviews')
def add_review():
    data = request.get_json()

    try:
        review = Review(
            text=data.get('text'),
            rating=data.get('rating'),
            user_id=data.get('user_id'),
            item_id=data.get('item_id')
        )

        db.session.add(review)
        db.session.commit()

        return review.to_dict(), 201
    
    except:
        return {'error': 'New review failed'}, 400
    

@app.post('/login')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return {'error': 'Please enter username and password'}, 400

    user = User.query.filter_by(username=username).first()

    if user:
        if user.authenticate(password):
            return user.to_dict(rules=('-password_hash')), 201

    session['user_id'] = user.id
    session['is_admin'] = user.admin

    return {'error': 'Username or password in incorrect'}, 400


if __name__ == '__main__':
    app.run(port=5555, debug=True)
