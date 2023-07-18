from config import db, SM

class Item(db.Model, SM):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    carts = db.relationship('ShoppingCart', backref='item')
    favorites = db.relationship('Favorite', backref='item')
    reviews = db.relationship('Review', backref='item')

    serialize_rules = ('-cart.item', '-favorites.item', '-reviews.item')

    def __repr__(self):
        return f'<Item {self.name}>'