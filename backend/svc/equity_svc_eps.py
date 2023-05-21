from flask_restx import Resource, Namespace
from flask_restx import reqparse

equity_ns_v1 = Namespace('equity', 'equity data service v1')
equity_ns_v2 = Namespace('equity', 'equity data service v2')


# @equity_ns_v2.route('/eps')
class EquityEPS(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ticker', type=str, help='Ticker')

    @equity_ns_v2.expect(parser)
    def get(self):
        args = self.parser.parse_args()
        ticker = args['ticker']
        if ticker is None:
            ticker = 'AAPL'

        data_aapl = [['2022.03', 6.15],
                  ['2022.06', 6.05],
                  ['2022.09', 6.11],
                  ['2022.12', 5.89],
                  ]

        data_msft = [['2022.03', 2.22],
                     ['2022.06', 2.24],
                     ['2022.09', 2.35],
                     ['2022.12', 2.20],
                    ]

        result = {'AAPL': data_aapl,
                  'MSFT': data_msft,
                  }

        return result


