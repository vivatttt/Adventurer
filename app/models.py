from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    hashtags = db.relationship('Hashtag', secondary='post_hashtag', backref='posts')

class Hashtag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

# Связующая таблица между постами и хэштегами (многие-ко-многим)
post_hashtag = db.Table('post_hashtag',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('hashtag_id', db.Integer, db.ForeignKey('hashtag.id'), primary_key=True)
)
