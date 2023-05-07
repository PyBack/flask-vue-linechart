import os
import site
import traceback

from flask import Flask, jsonify, request, session, Response
from flask import Blueprint
from flask_cors import CORS
from flask_restx import Api, Resource, reqparse
# from flask_bcrypt import Bcrypt
# from flask_sqlalchemy import SQLAlchemy

# from dotenv import load_dotenv

src_path = os.path.dirname(__file__)
pjt_home_path = os.path.join(src_path, os.pardir)
pjt_home_path = os.path.abspath(pjt_home_path)
site.addsitedir(pjt_home_path)
site.addsitedir(src_path)

# from utils.comn_logger import comn_logger
from equity_eps_svc import equity_eps_ns


def get_bp_v1() -> Blueprint:
    blueprint = Blueprint('api_1', __name__, url_prefix='/api/v1')
    api = Api(blueprint, title='Flask API v0.0', version='0.0', description='Flask API v0.0')
    api.add_namespace(equity_eps_ns)
    return blueprint


FLASK_RUN_PORT = 55000
FLASK_DEBUG = True

# 환경변수 로딩
# os.environ
# load_dotenv()

# instantiate the app
app = Flask(__name__)
api = Api(app, version='0.0',
          title='Flask API',
          description='A simple Flask API',
          )
app.register_blueprint(get_bp_v1())

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/health_check', methods=['GET'])
def health_check():
    return jsonify('good')


@app.route('/traceback_test', methods=['GET'])
def traceback_test_router():
    msg = 'ok'
    try:
        int('k')
    except:
        msg = traceback.format_exc()
        # comn_logger.error(msg)
        print(msg)
    return jsonify(msg)


@api.route('/echo')
class Hello(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Name')

    def get(self):
        args = self.parser.parse_args()
        msg = args['name']
        return 'message > ' + 'echo: %s' % msg


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=os.environ.get('FLASK_RUN_PORT'), debug=os.environ.get('FLASK_DEBUG'))
    app.run(host='0.0.0.0', port=FLASK_RUN_PORT, debug=FLASK_DEBUG)
