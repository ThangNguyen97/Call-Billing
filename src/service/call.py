from flask import request
from flask_restful import Resource
from config.config import get_config
from utils.db import insert_db
from utils.utils import handle_error, handle_success
import config.constants as const

config_app = get_config()


class Call(Resource):
    def __init__(self):
        Resource.__init__(self)

    @staticmethod
    def put(user_name):
        body_request = request.get_json()
        if len(user_name) > 32:
            return handle_error(const.ERROR['INVALID_USER_NAME'], 400)
        if "call_duration" not in body_request:
            return handle_error(const.ERROR['NOT_FOUND_CALL_DURATION'], 400)

        call_duration = body_request["call_duration"]
        if call_duration < 0:
            return handle_error(const.ERROR['INVALID_CALL_DURATION'], 400)
        insert_db(user_name, call_duration)
        return handle_success(const.SUCCESS['SUCCESS_CALL'], 200)
