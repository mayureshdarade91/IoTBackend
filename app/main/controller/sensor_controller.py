from flask import request
from flask_restx import Resource

from ..util.dto import SensorDto
from ..service.sensor_service import addNewSensor, getAllSensors, getASensor, getDeviceSensor
from app.main.util.decorator import tokenRequired

api = SensorDto.api
_sensor = SensorDto.sensor

@api.route('/')
class SensorList(Resource):
    @api.doc('list_of_registered_sensors')
    @tokenRequired
    @api.marshal_list_with(_sensor, envelope='data')
    def get(self):
        """List all registered sensors"""
        return getAllSensors()

    @api.response(201, 'Sensor successfully created.')
    @api.doc('create a new sensor')
    @tokenRequired
    @api.expect(_sensor, validate=True)
    def post(self):
        """Creates a new Sensor """
        data = request.json
        return addNewSensor(data=data)


@api.route('/<device_id>')
@api.param('device_id', 'The Device id')
@api.response(404, 'Sensor not found.')
class Sensor(Resource):
    @api.doc('get all sensors of device')
    @tokenRequired
    @api.marshal_with(_sensor)
    def get(self, device_id):
        """get a sensor given its identifier"""
        sensors = getDeviceSensor(device_id)
        if not sensors:
            api.abort(404)
        else:
            return sensors