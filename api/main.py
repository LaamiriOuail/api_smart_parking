from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_app import app
from models.client import Client
from models.abonement import Abonement
from models.car import Car
from database.database import db
from crud.client import get_clients_c,get_client_by_id_c,create_client_c,update_client_c,delete_client_c,get_client_cars
from crud.car import get_cars_c,get_car_by_id_c,create_car_c,update_car_c,delete_car_c,get_car_by_matricule_c,delete_car_by_matricule_c,get_car_ticket_by_id_c,get_car_ticket_by_matricule_c,get_cars_in_parking,get_number_cars_in_parking,get_number_cars
from crud.abonement import get_abonements_c,get_abonement_c,create_abonement_c,get_abonement_by_matricule_car_c,update_abonement_c,delete_abonement_c
with app.app_context():
    db.create_all()
##### CLIENT
@app.route('/clients', methods=['GET'])
def get_clients():
    return get_clients_c()

@app.route('/clients/<int:id>', methods=['GET'])
def get_client(id:int):
    return get_client_by_id_c(id)


@app.route('/clients', methods=['POST'])
def create_client():
    return create_client_c()

@app.route('/clients/<int:id>', methods=['PUT'])
def update_client(id:int):
    return update_client_c(id)


@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id:int):
    return delete_client_c(id)
@app.route('/clients/<int:id>/cars', methods=['GET'])
def get_cars_of_client(id:int):
    return get_client_cars(id)
###CARS
@app.route('/cars', methods=['GET'])
def get_cars():
    return get_cars_c()

@app.route('/cars/<int:id>', methods=['GET'])
def get_car(id:int):
    return get_car_by_id_c(id)

@app.route('/cars', methods=['POST'])
def create_car():
    return create_car_c()

@app.route('/cars/<int:id>', methods=['PUT'])
def update_car(id:int):
    return update_car_c(id)

@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    return delete_car_c(id)
@app.route('/cars/<string:matricule>', methods=['GET'])
def get_car_by_matricule(matricule):
    return get_car_by_matricule_c(matricule)
@app.route('/cars/<string:matricule>', methods=['DELETE'])
def delete_car_by_matricule(matricule):
    return delete_car_by_matricule_c(matricule)
@app.route('/cars/ticket/<int:id>', methods=['PUT'])
def get_car_ticket(id:int):
    return get_car_ticket_by_id_c(id)
@app.route('/cars/ticket/<string:matricule>', methods=['PUT'])
def get_car_ticket_matricule(matricule:str):
    return get_car_ticket_by_matricule_c(matricule)
@app.route('/cars/nbrinparking', methods=['GET'])
def get_car_number_in_parking():
    return get_number_cars_in_parking()
@app.route('/cars/inparking', methods=['GET'])
def get_in_parking_cars():
    return get_cars_in_parking()
@app.route('/cars/nbr', methods=['GET'])
def get_car_number():
    return get_number_cars()
### ABONEMENTS
@app.route('/abonements', methods=['GET'])
def get_abonements():
    return get_abonements_c()

@app.route('/abonements/<int:id>', methods=['GET'])
def get_abonement(id):
    return get_abonement_c(id)
@app.route('/abonements/cars/<string:matricule>', methods=['GET'])
def get_abonement_by_matricule_car(matricule:str):
    return get_abonement_by_matricule_car_c(matricule)
@app.route('/abonements', methods=['POST'])
def create_abonement():
    return create_abonement_c()

@app.route('/abonements/<int:id>', methods=['PUT'])
def update_abonement(id:int):
    return update_abonement_c(id)

@app.route('/abonements/<int:id>', methods=['DELETE'])
def delete_abonement(id:int):
    return delete_abonement_c(id)
if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1",port=8000)

