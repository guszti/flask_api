from app import ma
from marshmallow import fields

class DogSchema(ma.Schema):
    class Meta:
        fields =('name', 'species', 'age', 'created_at')

class SlaveSchema(ma.Schema):
    class Meta:
        fields =('sex', 'dog_id', 'created_at')