import datetime

from app.main import db
from app.main.model.sensor_data import SensorData

def addNewSensorData(data):
    new_user = SensorData(
        sensor_id=data['sensor_id'],
        sensor_data=data['sensor_data'],
        timestamp=datetime.datetime.utcnow()
    )
    saveChanges(new_user)
    response_object = {
        'status': 'success',
        'message': 'Successfully stored sensor data.'
    }
    return response_object, 201
    

def getAllSensorsData():
    return SensorData.query.all()


def getASensorDataAll(sensor_id):
    return SensorData.query.filter_by(sensor_id=sensor_id).all() 
    
def getASensorData(sensor_id,fromDateStr,toDateStr):
    fromDate = datetime.datetime.strptime(fromDateStr, '%Y-%m-%dT%H:%M:%S.%f')
    toDate = datetime.datetime.strptime(toDateStr, '%Y-%m-%dT%H:%M:%S.%f')
    return SensorData.query.filter(SensorData.sensor_id == sensor_id, SensorData.timestamp.between(fromDate,toDate)).all()

def saveChanges(data):
    db.session.add(data)
    db.session.commit()
