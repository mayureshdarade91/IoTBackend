from unicodedata import name
import uuid
import datetime

from app.main import db
from app.main.model.sensor import Sensor

def addNewSensor(data):
    sensor = Sensor.query.filter_by(name=data['name']).first()
    if not sensor:
        new_user = Sensor(
            device_id=data['device_id'],
            name=data['name'],
            registered_on=datetime.datetime.utcnow(),
            sensor_code = str(uuid.uuid4())
        )
        saveChanges(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered new sensor.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': "Sensor already exists with name : data['name']. Pleas use unique name for sensor.",
        }
        return response_object, 409


def getAllSensors():
    return Sensor.query.all()

def getASensor(name):
    return Sensor.query.filter_by(name=name).first()  

def getDeviceSensor(device_id):
    return Sensor.query.filter_by(device_id=device_id).all()

def saveChanges(data):
    db.session.add(data)
    db.session.commit()
