from app import db

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)

class Slave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String(80), nullable=False)
    dog_id = db.Column(db.Integer, db.ForeignKey('dog.id'))
