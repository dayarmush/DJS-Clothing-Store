from config import db, SM


class ShoppingCart(db.Model, SM):
    __tablename__ = 'shopping_carts'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    item = db.relationship('Item', backref='cart')

    serialize_rules = ('-user.cart', '-item.cart')

    def __repr__(self):
        return f'<Cart {self.id}'

