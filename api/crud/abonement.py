from models.abonement import Abonement
from models.car import Car
from flask import jsonify, request
from database.database import db 

def get_abonements_c():
    abonements = Abonement.query.all()
    abonement_data = [{
        'id': abonement.id,
        'create_at': abonement.create_at,
        'sold': abonement.sold,
        'car_id': abonement.car_id
    } for abonement in abonements]
    return jsonify(abonement_data), 200  # 200 OK
def get_abonement_c(id:int):
    try:
        abonement = Abonement.query.get_or_404(id)
        abonement_data = {
            'id': abonement.id,
            'create_at': abonement.create_at,
            'sold': abonement.sold,
            'car_id': abonement.car_id
        }
        return jsonify(abonement_data), 200  # 200 OK
    except:
        return jsonify({'message': f'Abonement not exist with this id {id}'}), 404  # 404 Not Found
def get_abonement_by_matricule_car_c(matricule:str):
    try:
        car = Car.query.filter_by(matricule=matricule).first_or_404()
        abonement = Abonement.query.filter_by(car_id=car.id).first_or_404()
        abonement_data = {
            'id': abonement.id,
            'create_at': abonement.create_at,
            'sold': abonement.sold,
            'car_id': abonement.car_id
        }
        return jsonify(abonement_data), 200  # 200 OK
    except:
        return jsonify({'message': f'Abonement not exist with this car matricule {matricule}'}), 404  # 404 Not Found
def create_abonement_c():
    sold = request.json.get('sold')
    car_id = request.json.get('car_id')
    if not all([sold, car_id]):
        return jsonify({'message': 'Incomplete data provided'}), 400  # 400 Bad Request

    existing_abonemnt = Abonement.query.filter_by(car_id=car_id).first()
    if existing_abonemnt:
        return jsonify({'message': 'Abonement already exists'}), 409  # 409 Conflict
    new_abonement = Abonement(
        sold=sold,
        car_id=car_id
    )
    db.session.add(new_abonement)
    db.session.commit()
    return jsonify({'message': 'Abonement created successfully'}), 201  # 201 Created
def update_abonement_c(id:int):
    try:
        abonement = Abonement.query.get_or_404(id)
        abonement.sold = request.json.get('sold',abonement.sold)
        abonement.car_id = request.json.get('car_id',abonement.car_id)
        db.session.commit()
        return jsonify({'message': 'Abonement updated successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Abonement not exist with this id {id}'}), 404  # 404 Not Found
def delete_abonement_c(id:int):
    try:
        abonement = Abonement.query.get_or_404(id)
        db.session.delete(abonement)
        db.session.commit()
        return jsonify({'message': 'Abonement deleted successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Abonement not exist with this id {id}'}), 404  # 404 Not Found












