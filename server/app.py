from models.favorites import Favorite
from models.items import Item
from models.reviews import Review
from models.shopping_cart import ShoppingCart
from models.user import User
from .config import Flask, Migrate, db
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

# Connecting the flask app to sqlalchemy db
db.init_app(app)

# Routes