from app import app, db
from flask import request, render_template, redirect, url_for, jsonify
from app.schemas import DogSchema, SubordinateSchema
from app.models import Dog, Subordinate
import json

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

@app.route('/api/subordinate', methods=['POST'])
def create_subordinate():
	if request.method == 'POST':
		sex = request.json['sex']
		dog_id = request.json['dog_id']

		slv = Subordinate(sex, dog_id)
		subordinate_schema = SubordinateSchema(strict=True)

		db.session.add(slv)
		db.session.commit()

		return subordinate_schema.jsonify(slv)

@app.route('/api/dogo', methods=['GET'])
def read_dogos():
	if request.method == 'GET':
		result = Dog.query.all()
		dog_schema = DogSchema(many=True)

		return dog_schema.jsonify(result)

@app.route('/api/subordinate', methods=['GET'])
def read_subordinates():
	if request.method == 'GET':
		result = Subordinate.query.all()
		subordinate_schema = SubordinateSchema(many=True)

		return subordinate_schema.jsonify(result)

@app.route('/api/dogo/<id>', methods=['POST'])
def read_dogo(id):
	if request.method == 'POST':
		result = Dog.query.get(id)
		dog_schema = DogSchema(strict=True)

		return dog_schema.jsonify(result)

@app.route('/api/subordinate/<id>', methods=['POST'])
def read_subordinate(id):
	if request.method == 'POST':
		result = Subordinate.query.get(id)
		subordinate_schema = SubordinateSchema(strict=True)

		return subordinate_schema.jsonify(result)

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

@app.route('/api/subordinate/<id>', methods=['PUT'])
def update_subordinate(id):
	if request.method == 'PUT':
		slv = Subordinate.query.get(id)

		slv.sex = request.json['sex']
		slv.dog_id = request.json['dog_id']
		
		subordinate_schema = SubordinateSchema(strict=True)

		db.session.commit()

		return subordinate_schema.jsonify(slv)

@app.route('/api/dogo/<id>', methods=['DELETE'])
def delete_dogo(id):
	if request.method == 'DELETE':
		dogo = Dog.query.get(id)

		db.session.delete(dogo)
		db.session.commit()

		return f'dogo {id} deleted successfully'

@app.route('/api/subordinate/<id>', methods=['DELETE'])
def delete_subordinate(id):
	if request.method == 'DELETE':
		slv = Subordinate.query.get(id)

		db.session.delete(slv)
		db.session.commit()

		return  f'subordinate {id} deleted successfully'
