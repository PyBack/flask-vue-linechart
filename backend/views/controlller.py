import logging

from flask import Blueprint
from flask_restx import Api, Namespace

from svc.equity_svc_eps import EquityEPS
from svc.equity_svc_sample import EquitySample


blueprint = Blueprint('api_2', __name__, url_prefix='/api/v2')
api = Api(blueprint, title='Flask API v0.2', version='0.2', description='Flask API v0.2')

equity_ns_v2 = Namespace('equity', 'equity data service v2')

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

stream_log = logging.StreamHandler()
stream_log.setFormatter(formatter)


def get_bp_v1() -> Blueprint:
    from svc.equity_svc_sample import equity_ns_v1
    blueprint = Blueprint('api_1', __name__, url_prefix='/api/v1')
    api = Api(blueprint, title='Flask API v0.1', version='0.1', description='Flask API v0.1')
    api.add_namespace(equity_ns_v1)
    return blueprint


def create_equity_namespace():
    api.add_namespace(equity_ns_v2)
    # equity_ns_v2.logger.setLevel(logging.DEBUG)
    # equity_ns_v2.logger.addHandler(stream_log)
    equity_ns_v2.add_resource(EquityEPS, '/eps')
    equity_ns_v2.add_resource(EquitySample, '/sample')
    equity_ns_v2.logger.setLevel(logging.DEBUG)
    equity_ns_v2.logger.debug('add resource')
