from app import app, db
from flask import request, render_template, redirect, url_for, jsonify
from app.schemas import DogSchema, SlaveSchema
from app.models import Dog, Slave


@app.route('/api/create', methods=['POST'])
def create():
    if request.method == 'POST':
        name = request.json['name']
        species = request.json['species']
        age = request.json['age']

        dogo = Dog(name, species, age)
        dog_schema = DogSchema(strict=True)

        db.session.add(dogo)
        db.session.commit()
    return dog_schema.jsonify(dogo)

@app.route('/api/read', methods=['GET'])
def read_all():
    return 'read all'

@app.route('/api/read/<id>', methods=['POST'])
def read(id):
    return f'read single {id}'

@app.route('/api/update/<id>', methods=['PUT'])
def update(id):
    return f'update {id}'

@app.route('/api/delete/<id>', methods=['DELETE'])
def delete(id):
    return f'delete {id}'