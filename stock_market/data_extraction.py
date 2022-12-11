import yfinance as yf
import pandas as pd
NSE_TICKER: list = ['NESTLEIND.NS',
                    'SUNPHARMA.NS',
                    'ITC.NS',
                    'DRREDDY.NS',
                    'TITAN.NS',
                    'EICHERMOT.NS',
                    'SBIN.NS',
                    'BPCL.NS',
                    'INDUSINDBK.NS',
                    'HDFCBANK.NS',
                    'HINDUNILVR.NS',
                    'HDFCLIFE.NS',
                    'BRITANNIA.NS',
                    'HDFC.NS',
                    'BHARTIARTL.NS',
                    'ASIANPAINT.NS',
                    'SBILIFE.NS',
                    'HEROMOTOCO.NS',
                    'ICICIBANK.NS',
                    'CIPLA.NS',
                    'TATACONSUM.NS',
                    'POWERGRID.NS',
                    'DIVISLAB.NS',
                    'ADANIPORTS.NS',
                    'KOTAKBANK.NS',
                    'BAJAJ-AUTO.NS',
                    'JSWSTEEL.NS',
                    'APOLLOHOSP.NS',
                    'COALINDIA.NS',
                    'GRASIM.NS',
                    'NTPC.NS',
                    'M&M.NS',
                    'ADANIENT.NS',
                    'LT.NS',
                    'MARUTI.NS',
                    'AXISBANK.NS',
                    'TATAMOTORS.NS',
                    'BAJFINANCE.NS',
                    'TATASTEEL.NS',
                    'BAJAJFINSV.NS',
                    'RELIANCE.NS',
                    'ONGC.NS',
                    'ULTRACEMCO.NS',
                    'HINDALCO.NS',
                    'UPL.NS',
                    'TCS.NS',
                    'WIPRO.NS',
                    'INFY.NS',
                    'TECHM.NS',
                    'HCLTECH.NS']


class HistoricalData():
    NSE_TICKER: list = ['NESTLEIND.NS',
                        'SUNPHARMA.NS',
                        'ITC.NS',
                        'DRREDDY.NS',
                        'TITAN.NS',
                        'EICHERMOT.NS',
                        'SBIN.NS',
                        'BPCL.NS',
                        'INDUSINDBK.NS',
                        'HDFCBANK.NS',
                        'HINDUNILVR.NS',
                        'HDFCLIFE.NS',
                        'BRITANNIA.NS',
                        'HDFC.NS',
                        'BHARTIARTL.NS',
                        'ASIANPAINT.NS',
                        'SBILIFE.NS',
                        'HEROMOTOCO.NS',
                        'ICICIBANK.NS',
                        'CIPLA.NS',
                        'TATACONSUM.NS',
                        'POWERGRID.NS',
                        'DIVISLAB.NS',
                        'ADANIPORTS.NS',
                        'KOTAKBANK.NS',
                        'BAJAJ-AUTO.NS',
                        'JSWSTEEL.NS',
                        'APOLLOHOSP.NS',
                        'COALINDIA.NS',
                        'GRASIM.NS',
                        'NTPC.NS',
                        'M&M.NS',
                        'ADANIENT.NS',
                        'LT.NS',
                        'MARUTI.NS',
                        'AXISBANK.NS',
                        'TATAMOTORS.NS',
                        'BAJFINANCE.NS',
                        'TATASTEEL.NS',
                        'BAJAJFINSV.NS',
                        'RELIANCE.NS',
                        'ONGC.NS',
                        'ULTRACEMCO.NS',
                        'HINDALCO.NS',
                        'UPL.NS',
                        'TCS.NS',
                        'WIPRO.NS',
                        'INFY.NS',
                        'TECHM.NS',
                        'HCLTECH.NS']

    def __init__(self, excluded: list = None) -> None:
        self.excluded = excluded
        self.ticker_list = NSE_TICKER
        if self.excluded is not None:
            self.ticker_list = [
                ticker for ticker in NSE_TICKER if ticker not in self.excluded]

    def get_data(self) -> pd.DataFrame:
        data = yf.download(self.ticker_list, period='max', group_by='ticker')
        return data


def save_data(data: pd.DataFrame, name: str) -> None:
    data.to_csv(name)


if __name__ == '__main__':
    hd = HistoricalData()
    conjugated_data = hd.get_data()
    for ticker in NSE_TICKER:
        save_data(conjugated_data[ticker].dropna(), f'../tickerData/{ticker}.csv')
