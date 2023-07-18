from config import db, SM

class Favorite(db.Model, SM):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)

    serialize_rules = ('-items.favorite', '-user.favorite')

    def __repr__(self):
        return f'<Favorite: {self.id}'
