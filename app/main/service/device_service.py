import uuid
import datetime

from app.main import db
from app.main.model.device import Device
from app.main.model.sensor import Sensor
from sqlalchemy import event


def addNewDevice(data):
    device = Device.query.filter_by(name=data['name']).first()
    if not device:
        new_user = Device(
            org_id=data['org_id'],
            name=data['name'],
            registered_on=datetime.datetime.utcnow(),
            device_code = str(uuid.uuid4())
        )
        saveChanges(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered new device.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': "Device already exists with name : " + data['name'] + " Pleas use unique name for device.",
        }
        return response_object, 409


def getAllDevices():
    return Device.query.all()

def getADevice(name):
    return Device.query.filter_by(name=name).first()

def updateDevice(name,data):
    device_rec = Device.query.filter_by(name=name).first()
    for key, value in data.items():
        if hasattr(Device, key):
            setattr(device_rec, key, value)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully updated device.'
    }
    return response_object, 201

@event.listens_for(Device, 'after_insert')
def addDefaultSensor(mapper, connection, target):
    ST = Sensor.__table__
    connection.execute(ST.insert().values(device_id=target.id,
                                          name='Temperature',
                                          registered_on=datetime.datetime.utcnow(),
                                          sensor_code = str(uuid.uuid4())
                                          ))
    connection.execute(ST.insert().values(device_id=target.id,
                                          name='Pressure',
                                          registered_on=datetime.datetime.utcnow(),
                                          sensor_code = str(uuid.uuid4())
                                          ))
    

def saveChanges(data):
    db.session.add(data)
    db.session.commit()
