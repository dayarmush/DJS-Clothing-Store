from ..config import db, SM

class Favorite(db.Model, SM):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.Datetime, onupdate=db.func.now())

    items = db.relationship('Item', backref='favorite')

    def __repr__(self):
        return f'<Favorite: {self.id}'
