import os
import pandas as pd

src_path = os.path.dirname(__file__)
pjt_home_path = os.path.join(src_path, os.pardir)
pjt_home_path = os.path.abspath(pjt_home_path)


def select_equity_eps(ticker: str):
    filepath = pjt_home_path + '/dao/'
    df = pd.read_csv(filepath + 'equity_eps.csv', sep='|', index_col=None)
    df_ticker = df[df['ticker'] == ticker][['date', 'eps']]

    df_ticker['date'] = df_ticker['date'].astype(str)
    data_ticker = df_ticker.values.tolist()

    return data_ticker


if __name__ == "__main__":
    df_result = select_equity_eps('AAPL')
    print(df_result)
    assert len(df_result) == 4
