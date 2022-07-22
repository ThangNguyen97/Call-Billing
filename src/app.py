from flask import Flask
from flask_restful import Api
import logging
from service.billing import Billing
from service.call import Call
from config.config import get_config

config_app = get_config()

app = Flask(__name__)
api = Api(app)

logging.basicConfig(filename=config_app['log']['app'],
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

api.add_resource(Call, "/mobile//<string:user_name>/call")
api.add_resource(Billing, "/mobile//<string:user_name>/billing")

app.run(host=config_app['server']['ip_address'], port=config_app['server']['port'], debug=False, threaded=True)
