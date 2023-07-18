from ..config import db, SM

class Review(db.Model, SM):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.Datetime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Review: {self.user} | {self.rating}'