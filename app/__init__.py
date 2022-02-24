import imp
from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.device_controller import api as device_ns
from .main.controller.sensor_controller import api as sensor_ns
from .main.controller.sensor_data_controller import api as sensor_data_ns


blueprint = Blueprint('api', __name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='IoT Assigment',
    version='1.0',
    description='Backend web service for IoT devices',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(device_ns, path='/device')
api.add_namespace(sensor_ns, path='/sensor')
api.add_namespace(sensor_data_ns, path='/sensor_data')