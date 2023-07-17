from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    review_relationship = db.Column(db.Boolean, default=False)
    admin = db.Column(db.Boolean, default=False)
    shopping_cart_relationship = db.Column(db.Boolean, default=False)
    favorites_relationship = db.Column(db.Boolean, default=False)


    shopping_cart = db.relationship('ShoppingCart', backref='user')
    favorites = db.relationship('Favorites', backref='user')
    reviews = db.relationship('Review', backref='user')