from flask import current_app
from flask_restx import Resource, Namespace
from flask_restx import reqparse

from dao.select_equity_eps import select_equity_eps

equity_ns_v1 = Namespace('equity', 'equity data service v1')
equity_ns_v2 = Namespace('equity', 'equity data service v2')


# @equity_ns_v2.route('/eps')
class EquityEPS(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ticker', type=str, help='Ticker')

    @equity_ns_v2.expect(parser)
    @equity_ns_v2.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def get(self):
        """
        AAPL, MSFT EPS 데이터 반환
        """
        args = self.parser.parse_args()
        ticker = args['ticker']
        if ticker is None:
            ticker = 'AAPL'

        data_aapl = select_equity_eps('AAPL')
        data_msft = select_equity_eps('MSFT')

        result = {'AAPL': data_aapl,
                  'MSFT': data_msft,
                  }

        current_app.logger.info(str(result))

        return result


