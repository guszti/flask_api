from app import ma
from marshmallow import Schema, fields

class DogSchema(ma.Schema):
    id = fields.Int()
    name = fields.Str()
    species = fields.Str()
    age = fields.Int()

class SlaveSchema(ma.Schema):
    id = fields.Int()
    sex = fields.Str()
    dog_id = fields.Int()