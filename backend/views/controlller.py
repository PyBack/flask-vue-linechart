from flask import current_app
from flask import Blueprint
from flask_restx import Api, Namespace
# from flask_request_validator import *
# from flask_request_validator.exceptions import InvalidRequestError
# from flask_request_validator.error_formatter import demo_error_formatter

from svc.equity_svc_eps import EquityEPS
from svc.equity_svc_sample import EquitySample


blueprint = Blueprint('api_2', __name__, url_prefix='/api/v2')
api = Api(blueprint, title='Flask API v0.2', version='0.2', description='Flask API v0.2')

equity_ns_v2 = Namespace('equity', 'equity data service v2')


@api.errorhandler
def default_error_handler(error):
    """
    Default error handler of api_2
    """
    # msg = traceback.format_exc()
    # Debug_mode: Ture 인 경우에 error 항목에 interactive debugger 모드가 생성됨
    # 따라서 Debug_mode: False 인 경우만 500 의 별도 메시지 출력 필요
    status_code = getattr(error, 'code', 500)
    msg = ''
    if current_app.debug is False & status_code == 500:
        msg = '관리자에게 문의'
    else:
        msg = str(error)

    return {'message': msg}, status_code


def get_bp_v1() -> Blueprint:
    from svc.equity_svc_sample import equity_ns_v1
    blueprint = Blueprint('api_1', __name__, url_prefix='/api/v1')
    api = Api(blueprint, title='Flask API v0.1', version='0.1', description='Flask API v0.1')
    api.add_namespace(equity_ns_v1)
    return blueprint


def create_equity_namespace():
    api.add_namespace(equity_ns_v2)

    equity_ns_v2.add_resource(EquityEPS, '/eps')
    equity_ns_v2.add_resource(EquitySample, '/sample')
