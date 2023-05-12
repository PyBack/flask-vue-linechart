from flask_restx import Resource, Namespace
from flask_restx import reqparse

equity_ns_v1 = Namespace('equity', 'equity data service v1')


# @equity_ns_v1.route('/sample')
class EquitySample(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ticker', type=str, help='Ticker')

    @equity_ns_v1.expect(parser)
    def get(self):
        args = self.parser.parse_args()
        ticker = args['ticker']

        return ticker
