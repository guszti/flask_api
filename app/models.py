from app import db
from datetime import datetime

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Slave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    dog_id = db.Column(db.Integer, db.ForeignKey('dog.id'))
