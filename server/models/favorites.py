from config import db, SM

# favorites class connects 
# a user and an item

class Favorite(db.Model, SM):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)

    serialize_rules = ('-item.favorites', '-item.reviews', '-item.carts', 
                       '-user.carts', '-user.reviews', '-user.carts')

    def __repr__(self):
        return f'<Favorite: {self.id}'
