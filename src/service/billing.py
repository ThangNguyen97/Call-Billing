from flask import request, jsonify
from flask_restful import Resource
from utils.db import get_db_by_user
from utils.utils import handle_error
import config.constants as const
from config.config import get_config
from math import ceil

config_app = get_config()


class Billing(Resource):
    def __init__(self):
        Resource.__init__(self)

    @staticmethod
    def get(user_name):
        datas = get_db_by_user(user_name)
        if len(datas) == 0:
            return handle_error(const.ERROR['NOT_FOUND_USER_NAME'].format(user_name), 400)

        call_durations = [data[1] for data in datas]
        call_count = sum(call_durations)
        block_count = sum([call_duration(i / 30000) for call_duration in call_durations])
        return jsonify({'call_count': call_count, 'block_count': block_count})
