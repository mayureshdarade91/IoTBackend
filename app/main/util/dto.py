from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class DeviceDto:
    api = Namespace('device', description='device related operations')
    device = api.model('device', {
        'id': fields.Integer(required=False, description='ID'),
        'name': fields.String(required=True, description='Device Name'),
        'org_id': fields.Integer(required=True, description='Organisation ID'),
        'device_code': fields.String(required=False, description='Device Code'),
        'registered_on': fields.DateTime(required=False, description='Register Date'),
        'last_active': fields.DateTime(required=False, description='Last Active'),
    })

class SensorDto:
    api = Namespace('sensor', description='sensor related operations')
    sensor = api.model('sensor', {
        'id': fields.Integer(required=False, description='ID'),
        'name': fields.String(required=True, description='Sensor Name'),
        'device_id': fields.Integer(required=True, description='Device ID'),
        'sensor_code': fields.String(required=False, description='Sensor Code'),
        'registered_on': fields.DateTime(required=False, description='Register Date'),
        'last_active': fields.DateTime(required=False, description='Last Active'),
    })

class SensorDataDto:
    api = Namespace('sensor_data', description='sensor related operations')
    sensor_data = api.model('sensor_data', {
        'id': fields.Integer(required=False, description='ID'),
        'sensor_id': fields.Integer(required=True, description='Sensor ID'),
        'sensor_data': fields.Integer(required=True, description='Sensor Data'),
        'timestamp': fields.DateTime(required=False, description='Register Date')
    })