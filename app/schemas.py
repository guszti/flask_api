from app import ma
from marshmallow import fields
from app.models import Dog, Slave

class DogSchema(ma.Schema):
    class Meta:
        model = Dog
        fields = ('id', 'name', 'species', 'age', 'created_at')

class SlaveSchema(ma.Schema):
    class Meta:
        model = Slave
        fields = ('id', 'sex', 'dog_id', 'created_at')
