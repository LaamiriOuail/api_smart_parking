from models.client import Client
from models.car import Car
from flask import jsonify, request
from database.database import db 

def get_cars_c():
    cars = Car.query.all()
    car_data = [{
        'id': car.id,
        'matricule': car.matricule,
        'is_in_parking': car.is_in_parking,
        'model': car.model,
        'client_id': car.client_id,
        'abonement': {'id': car.abonement.id if car.abonement else None}
    } for car in cars]
    return jsonify(car_data), 200  # 200 OK 
def create_car_c():
    client_id = request.json.get('client_id')
    if Client.client_exists_by_id(client_id):
        matricule = request.json.get('matricule')
        is_in_parking = request.json.get('is_in_parking')
        model = request.json.get('model')
        if not all([matricule, model, client_id]):
            return jsonify({'message': 'Incomplete data provided'}), 400  # 400 Bad Request

        existing_car = Car.query.filter_by(matricule=matricule).first()
        if existing_car:
            return jsonify({'message': 'Car already exists'}), 409  # 409 Conflict

        new_car = Car(matricule=request.json.get('matricule'),is_in_parking=request.json.get('is_in_parking'),model=request.json.get('model'),client_id=request.json.get('client_id'))
        db.session.add(new_car)
        db.session.commit()

        return jsonify({'message': 'Car created successfully'}), 201  # 201 Created
    else:
         return jsonify({'message': f'Client not exist with this id {request.json.get("client_id")}'}), 404  # 404 Not Found
def update_car_c(id:int):
    try:
        car = Car.query.get(id)
        car.matricule = request.json.get('matricule', car.matricule)
        car.is_in_parking = request.json.get('is_in_parking', car.is_in_parking)
        car.model = request.json.get('model', car.model)
        car.client_id = request.json.get('client_id', car.client_id)
        db.session.commit()
        return jsonify({'message': 'Car updated successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this id {id}'}), 404  # 404 Not Found
def delete_car_c(id:int):
    try:
        car = Car.query.get(id)
        db.session.delete(car)
        db.session.commit()
        return jsonify({'message': 'Car deleted successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this id {id}'}), 404  # 404 Not Found    
def get_car_by_id_c(id:int):
    try:
        car = Car.query.get(id)
        car_data = {
            'id': car.id,
            'matricule': car.matricule,
            'is_in_parking': car.is_in_parking,
            'model': car.model,
            'client_id': car.client_id,
            'abonement': {'id': car.abonement.id if car.abonement else None}
        }
        return jsonify(car_data), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this id {id}'}), 404  # 404 Not Found
def delete_car_by_matricule_c(matricule: str):
    try:
        car = Car.query.filter_by(matricule=matricule).first_or_404()
        db.session.delete(car)
        db.session.commit()
        return jsonify({'message': 'Car deleted successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this matricule {matricule}'}), 404  # 404 Not Found
def get_car_by_matricule_c(matricule: str):
    try:
        car = Car.query.filter_by(matricule=matricule).first_or_404()
        car_data = {
            'id': car.id,
            'matricule': car.matricule,
            'is_in_parking': car.is_in_parking,
            'model': car.model,
            'client_id': car.client_id,
            'abonement': {'id': car.abonement.id if car.abonement else None}
        }
        return jsonify(car_data), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this matricule {matricule}'}), 404  # 404 Not Found
def get_car_ticket_by_id_c(id:int):
    try:
        ticket=12
        car = Car.query.get(id)
        if not car.is_in_parking:
            car.is_in_parking = True
            car.abonement.sold-=ticket
            db.session.commit()
            return jsonify({'message': 'Car ticket successfully take'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this id {id}'}), 404  # 404 Not Found
def get_car_ticket_by_matricule_c(matricule:str):
    try:
        ticket=12
        car = car = Car.query.filter_by(matricule=matricule).first_or_404()
        if not car.is_in_parking:
            car.is_in_parking = True
            car.abonement.sold-=ticket
            db.session.commit()
            return jsonify({'message': 'Car ticket successfully take'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this matricule {matricule}'}), 404  # 404 Not Found
def get_number_cars_in_parking():
    number=0
    cars = Car.query.all()
    for car in cars:
        if car.is_in_parking:
            number+=1
    return jsonify({"number":f"{number}"}), 200  # 200 OK 
def get_cars_in_parking():
    cars = Car.query.all()
    car_data = [{
        'id': car.id,
        'matricule': car.matricule,
        'is_in_parking': car.is_in_parking,
        'model': car.model,
        'client_id': car.client_id,
        'abonement': {'id': car.abonement.id if car.abonement else None}
    } for car in cars if car.is_in_parking]
    return jsonify(car_data), 200  # 200 OK 
def get_number_cars():
    cars = Car.query.all()
    return jsonify({"number":f"{len(cars)}"}), 200  # 200 OK 















