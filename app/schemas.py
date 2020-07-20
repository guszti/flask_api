from app import ma
from marshmallow import fields
from app.models import Dog, Subordinate

class SubordinateSchema(ma.Schema):
    class Meta:
        model = Subordinate
        fields = ('id', 'sex', 'dog_id', 'created_at')

class DogSchema(ma.Schema):
    class Meta:
        model = Dog
        fields = ('id', 'name', 'species', 'age', 'created_at', 'subordinates')
    subordinates = ma.Nested(SubordinateSchema, many=True)