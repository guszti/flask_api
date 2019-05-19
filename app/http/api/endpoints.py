from app import app, db
from flask import request, render_template, redirect, url_for, jsonify
from app.schemas import DogSchema, SlaveSchema
from app.models import Dog, Slave


@app.route('/api/dogo', methods=['POST'])
def create_dogo():
    if request.method == 'POST':
        name = request.json['name']
        species = request.json['species']
        age = request.json['age']

        dogo = Dog(name, species, age)
        dog_schema = DogSchema(strict=True)

        db.session.add(dogo)
        db.session.commit()

        return dog_schema.jsonify(dogo)

@app.route('/api/slave', methods=['POST'])
def create_slave():
    if request.method == 'POST':
        sex = request.json['sex']
        dog_id = request.json['dog_id']

        slv = Slave(sex, dog_id)
        slave_schema = SlaveSchema(strict=True)

        db.session.add(slv)
        db.session.commit()

        return slave_schema.jsonify(slv)

@app.route('/api/dogo', methods=['GET'])
def read_dogos():
    return 'all dogs'

@app.route('/api/slave', methods=['GET'])
def read_slaves():
    return 'all slaves'

@app.route('/api/dogo/<id>', methods=['POST'])
def read_dogo(id):
    return f'read single {id}'

@app.route('/api/slave/<id>', methods=['POST'])
def read_slave(id):
    return f'read single {id}'

@app.route('/api/dogo/<id>', methods=['PUT'])
def update_dogo(id):
    return f'update {id}'

@app.route('/api/slave/<id>', methods=['PUT'])
def update_slave(id):
    return f'update {id}'

@app.route('/api/dogo/<id>', methods=['DELETE'])
def delete_dogo(id):
    return f'delete {id}'

@app.route('/api/slave/<id>', methods=['DELETE'])
def delete_slave(id):
    return f'delete {id}'