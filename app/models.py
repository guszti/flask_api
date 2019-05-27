from app import db
from datetime import datetime

class Dog(db.Model):
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    slaves = db.relationship('Slave')

class Slave(db.Model):
    def __init__(self, sex, dog_id):
        self.sex = sex
        self.dog_id = dog_id

    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    dog_id = db.Column(db.Integer, db.ForeignKey('dog.id'))
