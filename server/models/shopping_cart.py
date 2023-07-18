from ..config import db, SM

class ShoppingCart(db.Model, SM):
    __tablename__ = 'shopping_carts'


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    item = db.relationship('Item', backref='cart')

    def __repr__(self):
        return f'<Cart {self.id}'
