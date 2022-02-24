from functools import wraps

from flask import request

from app.main.service.auth_helper import Auth
from typing import Callable


def tokenRequired(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.getLoggedInUser(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated
