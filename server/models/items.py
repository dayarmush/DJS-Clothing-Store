from ..config import db, SM

class Item(db.Model, SM):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.Datetime, onupdate=db.func.now())

    reviews = db.relationship('Review', backref='item')

    def __repr__(self):
        return f'<Item {self.name}>'