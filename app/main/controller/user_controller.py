from flask import request
from flask_restx import Resource

from app.main.util.decorator import tokenRequired
from ..util.dto import UserDto
from ..service.user_service import addNewUser, getAllUsers, getAUser
from typing import Dict, Tuple

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @tokenRequired
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return getAllUsers()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new User """
        data = request.json
        return addNewUser(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = getAUser(public_id)
        if not user:
            api.abort(404)
        else:
            return user



