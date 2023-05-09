from flask_restx import Resource, Namespace
from flask_restx import reqparse

equity_eps_ns = Namespace('equity_eps', 'equity eps data service')


@equity_eps_ns.route('/')
class EquityEPS(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ticker', type=str, help='Ticker')

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


