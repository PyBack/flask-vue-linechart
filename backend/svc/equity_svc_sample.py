from flask_restx import Resource, Namespace
from flask_restx import reqparse

equity_ns_v1 = Namespace('equity', 'equity data service v1')
equity_ns_v2 = Namespace('equity', 'equity data service v2')


# @equity_ns_v2.route('/sample')
class EquitySample(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ticker', type=str, help='Ticker')

    @equity_ns_v2.expect(parser)
    def get(self):
        """
        Ticker 이름 echo 기능
        """
        args = self.parser.parse_args()
        ticker = args['ticker']

        return ticker
