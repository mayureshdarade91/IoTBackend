from unicodedata import name
from xmlrpc.client import DateTime
from flask import request
from flask_restx import Resource, reqparse, fields


from ..util.dto import SensorDataDto, SensorDataFilterDto
from ..service.sensor_data_service import addNewSensorData, getAllSensorsData, getASensorData, getASensorDataAll
from app.main.util.decorator import tokenRequired

api = SensorDataDto.api
_sensor = SensorDataDto.sensor_data


resource_fields = api.model('Resource', {
    'sensor_id': fields.Integer,
    'from':fields.DateTime,
    'to':fields.DateTime
})

@api.route('/')
class SensorList(Resource):
    @api.doc('list_of_registered_sensors')
    @tokenRequired
    @api.marshal_list_with(_sensor, envelope='data')
    def get(self):
        """List all registered sensors"""
        return getAllSensorsData()

    @api.response(201, 'Sensor successfully created.')
    @api.doc('create a new sensor')
    @api.expect(_sensor, validate=True)
    def post(self):
        """Creates a new Sensor """
        data = request.json
        return addNewSensorData(data=data)


@api.route('/<sensor_id>')
@api.param('sensor_id', 'The Sensor identifier')
@api.response(404, 'Sensor not found.')
class Sensor(Resource):
    @api.doc('get a sensor')
    @tokenRequired
    @api.marshal_with(_sensor)
    def get(self, sensor_id):
        """get all sensor data"""
        sensor_data = getASensorDataAll(sensor_id)
        if not sensor_data:
            api.abort(404)
        else:
            return sensor_data

@api.route('/filter_data')
@api.response(404, 'Sensor Data not found.')
class Sensor(Resource):
    @api.doc('Get Sensor data in Date Range')
    @api.marshal_list_with(_sensor)
    @api.expect(resource_fields, validate=True)
    def post(self):
        """ Get Sensor data in Date Range """
        data = request.json
        return getASensorData(data['sensor_id'],data['from'],data['to'])
        