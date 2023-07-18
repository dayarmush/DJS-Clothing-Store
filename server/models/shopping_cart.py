from config import db, SM

# Shopping cart is the middle table
# to connect user with aan item

class ShoppingCart(db.Model, SM):
    __tablename__ = 'shopping_carts'


    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)

    serialize_rules = ('-user.cart', '-item.cart')

    def __repr__(self):
        return f'<Cart {self.id}'
