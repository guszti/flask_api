from app import app
from flask import request, render_template, redirect, url_for

@app.route('/api/create', methods=['POST'])
def create():
    return 'create'

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