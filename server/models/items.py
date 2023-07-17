from ..config import db, SM

class Item(db.Model, SM):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    reviews = db.relationship('Review', backref='items')

    def __repr__(self):
        return f'<Item {self.name}>'