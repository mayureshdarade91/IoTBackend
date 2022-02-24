from unicodedata import name
from flask import request
from flask_restx import Resource

from ..util.dto import DeviceDto
from ..service.device_service import addNewDevice, getAllDevices, getADevice, updateDevice
from app.main.util.decorator import tokenRequired

api = DeviceDto.api
_device = DeviceDto.device


@api.route('/')
class DeviceList(Resource):
    @api.doc('list_of_registered_devices')
    @tokenRequired
    @api.marshal_list_with(_device, envelope='data')
    def get(self):
        """List all registered devices"""
        return getAllDevices()

    @api.response(201, 'Device successfully created.')
    @api.doc('Create a new Device')
    @tokenRequired
    @api.expect(_device, validate=True)
    def post(self):
        """Creates a new Device """
        data = request.json
        return addNewDevice(data=data)


@api.route('/<name>')
@api.param('name', 'The Device identifier')
@api.response(404, 'Device not found.')
class Device(Resource):
    @api.doc('get a device')
    @tokenRequired
    @api.marshal_with(_device)
    def get(self, name):
        """get a device given its identifier"""
        device = getADevice(name)
        if not device:
            api.abort(404)
        else:
            return device
    
    @api.response(201, 'Device updated successfully.')
    @api.doc('Update Device')
    @tokenRequired
    @api.expect(_device, validate=True)
    def put(self,name):
        """ Update Device """
        data = request.json
        return updateDevice(name,data=data)