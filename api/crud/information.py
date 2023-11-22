from models.car import Car
from models.abonement import Abonement
from models.client import Client
from flask import jsonify

def get_information():
    clients=Client.query.all()
    list_info:list=[]
    if clients:
        i:int=0
        for client in clients:
            cars_client=Car.query.filter_by(client_id=client.id).all()
            if cars_client :
                have_cars=1
                for car in cars_client:
                    if car.abonement:
                        abonement=Abonement.query.filter_by(id=car.abonement.id).first()
                        abonement_sold=abonement.sold
                        abonement_create_at=abonement.create_at
                        have_abonement=1
                    else :
                        abonement_sold=0
                        abonement_create_at=client.create_at
                        have_abonement=0
                    i=i+1
                    list_info.append({
                        "id": i,
                        "fullname":client.fullname,
                        "cin":client.cin,
                        "email":client.email,
                        "phone_number":client.phone_number,
                        "age":client.age,
                        "sold":abonement_sold,
                        "create_at":abonement_create_at,
                        "model":car.model,
                        "matricule":car.matricule,
                        "is_in_parking":car.is_in_parking,
                        "have_abonement":have_abonement,
                        "have_cars":have_cars
                    })
            else:
                i=i+1
                have_cars=0
                have_abonement=0
                list_info.append({
                    "id": i,
                    "fullname":client.fullname,
                    "cin":client.cin,
                    "email":client.email,
                    "phone_number":client.phone_number,
                    "age":client.age,
                    "sold":0,
                    "create_at":client.create_at,
                    "model":0,
                    "matricule":0,
                    "is_in_parking":0,
                    "have_abonement":have_abonement,
                    "have_cars":have_cars

                })
    return jsonify(list_info),200

def get_information_by_user_id(matricule:str):
    client_id=Car.query.filter_by(matricule=matricule).first().id
    client=Client.query.filter_by(id=client_id).first()

    info:dict={
                    "id": "",
                    "fullname":"",
                    "cin":"",
                    "email":"",
                    "phone_number":"",
                    "age":"",
                    "sold":"",
                    "create_at":"",
                    "model":"",
                    "matricule":"",
                    "is_in_parking":"",
                    "have_abonement":"",
                    "have_cars":""
                }
    if client:
        i:int=0
        car=Car.query.filter_by(matricule=id).first()
        if car :
            have_cars=1
            if car.abonement:
                abonement=Abonement.query.filter_by(id=car.abonement.id).first()
                abonement_sold=abonement.sold
                abonement_create_at=abonement.create_at
                have_abonement=1
            else :
                abonement_sold=0
                abonement_create_at=client.create_at
                have_abonement=0
            i=i+1
            info={
                    "id": i,
                    "fullname":client.fullname,
                    "cin":client.cin,
                    "email":client.email,
                    "phone_number":client.phone_number,
                    "age":client.age,
                    "sold":abonement_sold,
                    "create_at":abonement_create_at,
                    "model":car.model,
                    "matricule":car.matricule,
                    "is_in_parking":car.is_in_parking,
                    "have_abonement":have_abonement,
                    "have_cars":have_cars
            }
    else:
        i=i+1
        have_cars=0
        have_abonement=0
        info={
            "id": i,
                "fullname":client.fullname,
                "cin":client.cin,
                "email":client.email,
                "phone_number":client.phone_number,
                "age":client.age,
                "sold":0,
                "create_at":client.create_at,
                "model":0,
                "matricule":0,
                "is_in_parking":0,
                "have_abonement":have_abonement,
                "have_cars":have_cars
            }
    return jsonify(info),200        
