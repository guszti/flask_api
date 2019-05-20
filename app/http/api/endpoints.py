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
	if request.method == 'GET':
		result = Dog.query.all()
		dog_schema = DogSchema(many=True)

		return dog_schema.jsonify(result)

@app.route('/api/slave', methods=['GET'])
def read_slaves():
	if request.method == 'GET':
		result = Slave.query.all()
		slave_schema = SlaveSchema(many=True)

		return slave_schema.jsonify(result)

@app.route('/api/dogo/<id>', methods=['POST'])
def read_dogo(id):
	if request.method == 'POST':
		result = Dog.query.get(id)
		dog_schema = DogSchema(strict=True)

		return dog_schema.jsonify(result)

@app.route('/api/slave/<id>', methods=['POST'])
def read_slave(id):
	if request.method == 'POST':
		result = Slave.query.get(id)
		slave_schema = SlaveSchema(strict=True)

		return slave_schema.jsonify(result)

@app.route('/api/dogo/<id>', methods=['PUT'])
def update_dogo(id):
	if request.method == 'PUT':
		dogo = Dog.query.get(id)

		dogo.name = request.json['name']
		dogo.species = request.json['species']
		dogo.age = request.json['age']
		
		dog_schema = DogSchema(strict=True)

		db.session.commit()

		return dog_schema.jsonify(dogo)

@app.route('/api/slave/<id>', methods=['PUT'])
def update_slave(id):
	if request.method == 'PUT':
		slv = Slave.query.get(id)

		slv.sex = request.json['sex']
		slv.dog_id = request.json['dog_id']
		
		slave_schema = SlaveSchema(strict=True)

		db.session.commit()

		return slave_schema.jsonify(slv)

@app.route('/api/dogo/<id>', methods=['DELETE'])
def delete_dogo(id):
	if request.method == 'DELETE':
		dogo = Dog.query.get(id)

		db.session.delete(dogo)
		db.session.commit()

		return f'dogo {id} deleted successfully'

@app.route('/api/slave/<id>', methods=['DELETE'])
def delete_slave(id):
	if request.method == 'DELETE':
		slv = Slave.query.get(id)

		db.session.delete(slv)
		db.session.commit()

		return  f'slave {id} deleted successfully'
