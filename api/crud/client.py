from models.client import Client
from models.car import Car
from flask import jsonify, request
from database.database import db 

def get_clients_c():
    clients = Client.query.all()
    client_data = []
    for client in clients:
        client_data.append({
            'id': client.id,
            'fullname': client.fullname,
            'email': client.email,
            'phone_number': client.phone_number,
            'cin': client.cin,
            'age': client.age,
            'create_at': client.create_at
        })
    return jsonify(client_data), 200  # 200 OK

def get_client_by_id_c(id:int):
    try:
        client = Client.query.get(id)
        client_data = {
            'id': client.id,
            'fullname': client.fullname,
            'email': client.email,
            'phone_number': client.phone_number,
            'cin': client.cin,
            'age': client.age,
            'create_at': client.create_at
        }
        return jsonify(client_data), 200  # 200 OK
    except:
        return jsonify({'message': f'Client not exist with this id {id}'}), 404  # 404 Not Found

def create_client_c():
    fullname = request.json.get('fullname')
    email = request.json.get('email')
    phone_number = request.json.get('phone_number')
    cin = request.json.get('cin')
    age = request.json.get('age')

    if not all([fullname, email, phone_number, cin, age]):
        return jsonify({'message': 'Incomplete data provided'}), 400  # 400 Bad Request

    existing_client = Client.query.filter_by(cin=cin).first()
    if existing_client:
        return jsonify({'message': 'Client already exists'}), 409  # 409 Conflict

    new_client = Client(fullname=fullname, email=email, phone_number=phone_number, cin=cin, age=age)
    db.session.add(new_client)
    db.session.commit()

    return jsonify({'message': 'Client created successfully'}), 201  # 201 Created

def update_client_c(id:int):
    try:
        client = Client.query.get(id)
        client.fullname = request.json.get('fullname', client.fullname)
        client.email = request.json.get('email', client.email)
        client.phone_number = request.json.get('phone_number', client.phone_number)
        client.cin = request.json.get('cin', client.cin)
        client.age = request.json.get('age', client.age)
        db.session.commit()
        return jsonify({'message': 'Client updated successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Client not exist with this id {id}'}), 404  # 404 Not Found

def delete_client_c(id:int):
    try:
        client = Client.query.get(id)
        db.session.delete(client)
        db.session.commit()
        return jsonify({'message': 'Client deleted successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Client not exist with this id {id}'}), 404  # 404 Not Found

def get_client_cars(id:int):
    cars = Car.query.all()
    car_data = [{
        'id': car.id,
        'matricule': car.matricule,
        'is_in_parking': car.is_in_parking,
        'model': car.model,
        'abonement': {'id': car.abonement.id if car.abonement else None}
    } for car in cars if car.client_id==id]
    return jsonify(car_data), 200  # 200 OK 