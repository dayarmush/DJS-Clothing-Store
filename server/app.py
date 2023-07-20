from models.favorites import Favorite
from models.items import Item
from models.reviews import Review
from models.shopping_cart import ShoppingCart
from models.user import User
from config import Flask, Migrate, db, request, session, CORS, render_template
from dotenv import load_dotenv
import os

# sys.path.append('/opt/render/project/src/server')

load_dotenv()

# Create Flask Instance
app = Flask(
    __name__,
    static_url_path='/' #,
    # static_folder='../client/build',
    # template_folder='../client/build'
)

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

CORS(app)

# Routes
# @app.route('/')
# def index():
#     return render_template("index.html")

@app.post('/signup')
def post_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return {'error': 'Please enter a username and password'}, 400

    user = User.query.filter_by(username=username).first()

    if user:
        return {'error': 'Username already exists'}, 400

    try:
        user = User(
            username=data.get('username'),
            # admin=True
        )

        user.password_hash = data.get('password')

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id

        if user.admin:
            session['is_admin'] = user.admin

        return user.to_dict(), 201
    
    except:
        return {'error': 'Signup failed'}, 400

# Only accessible when logged in 
@app.post('/carts')
def add_cart():
    data = request.get_json()

    try:
        cart = ShoppingCart(
            user_id=data.get('user_id'),
            item_id=data.get('item_id')
        )

        db.session.add(cart)
        db.session.commit()

        return cart.to_dict(), 201
    
    except:
        return {'error': 'Add to cart failed'}, 400

# Only accessible when logged in 
@app.delete('/carts/<int:id>')
def delete_cart(id):

    cart = ShoppingCart.query.filter_by(id=id).first()

    if not cart:
        return {'error': 'cart not found'}
    
    db.session.delete(cart)
    db.session.commit()

    return {}, 200

# Only accessible when logged in 
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
    
# Only accessible when logged in 
@app.delete('/reviews/<int:id>')
def delete_reviews(id):
    review = Review.query.filter_by(id=id).first()

    if not review:
        return {'error': 'No review found'}, 404
    
    db.session.delete(review)
    db.session.commit()

    return {}, 202

@app.get('/items')
def get_items():
    items = Item.query.all()

    return [item.to_dict() for item in items], 200

# Admin access only
@app.post('/items')
def add_item():
    data = request.get_json()

    try:
        item = Item(
            name=data.get('name'),
            image=data.get('image'),
            price=data.get('price'),
            category=data.get('category')
        )

        db.session.add(item)
        db.session.commit()

        return item.to_dict(), 201
    
    except:
        return {'error': 'failed to add item'}, 400
    
# Admin access only
@app.route('/items/<int:id>', methods=['DELETE', 'PATCH', 'GET'])
def items_by_id(id):
    item = Item.query.filter_by(id=id).first()

    if not item:
        return {'error': 'No item found'}, 404
    
    if request.method == 'DELETE':
        try:
            db.session.delete(item)
            db.session.commit()

            return {}, 202
        
        except:
            return {'error': 'Failed to delete'}, 404
        
    if request.method == 'PATCH':
        data = request.get_json()

        try:
            for key in data:
                setattr(item, key, data[key])

            db.session.add(item)
            db.session.commit()

            return item.to_dict(), 201
        except:
            return {'error': 'Edit failed'}
        
    if request.method == 'GET':
        return item.to_dict(), 200

# This route is for testing purposes       
@app.get('/users')
def get_users():
    users = User.query.all()

    return [user.to_dict(rules=('-_password_hash',)) for user in users], 200

# Only accessible when logged in 
@app.post('/favorites')
def add_favorite():
    data = request.get_json()

    try:
        fave = Favorite(
            user_id=data.get('user_id'),
            item_id=data.get('item_id')
        )

        db.session.add(fave)
        db.session.commit()

        return fave.to_dict(), 201
    
    except:
        return {'error': 'Failed to add favorite'}
    
# Only accessible when logged in 
@app.delete('/favorites/<int:id>')
def delete_fave(id):
    fave = Favorite.query.filter_by(id=id).first()

    if not fave:
        return {'error': 'No favorite found'}, 404
    
    db.session.delete(fave)
    db.session.commit()

    return {}, 202

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
            session['user_id'] = user.id
            if user.admin:
                session['is_admin'] = user.admin
            return user.to_dict(rules=('-_password_hash',)), 201
        
    return {'error': 'Username or password is incorrect'}, 400

# Only accessible when logged in 
@app.delete('/logout')
def logout():
    if session.get('user_id'):
        session.clear()
        return {}, 200

    return {'error': 'Please log in'}

@app.get('/items/mens')
def get_mens_items():
    items = Item.query.filter_by(category="Men's").all()

    return [item.to_dict() for item in items], 200

@app.get('/items/womens')
def get_womens_items():
    items = Item.query.filter_by(category="Women's").all()
    return [item.to_dict() for item in items]

@app.get('/items/kids')
def get_kids_items():
    items = Item.query.filter_by(category="kids").all()
    return [item.to_dict() for item in items]

@app.get('/check_session')
def Check_session():
    if session.get('user_id'):
        user = User.query.filter_by(id=session.get('user_id')).first()
        return user.to_dict(), 200
    
    return {'error': 'not logged in'}, 401


if __name__ == '__main__':
    app.run(port=5555, debug=True)
