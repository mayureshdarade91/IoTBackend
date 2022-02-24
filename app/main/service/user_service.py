from signal import pthread_kill
import uuid
import datetime

from app.main import db
from app.main.model.user import User
from typing import Dict, Tuple


def addNewUser(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password']
        )
        saveChanges(new_user)
        return generateToken(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def getAllUsers():
    return User.query.all()


def getAUser(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generateToken(user: User) -> Tuple[Dict[str, str], int]:
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def saveChanges(data: User) -> None:
    db.session.add(data)
    db.session.commit()

