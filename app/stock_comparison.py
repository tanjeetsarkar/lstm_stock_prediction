from Learningapp.tickers import Tickers
from stock_prediction import StockPrediction
from data_extraction import HistoricalData
from tensorflow.keras.models import load_model

tickers = Tickers()


class BestStocks():
    NSETICKERS: list = tickers.NSE_TICKER
    TICKER_DATASET_PATH: str = 'Learningapp/tickerData/'
    TICKER_MODEL_PATH: str = 'Learningapp/models/'

    def __init__(self, extended_model_path: str = '', excluded: list = []) -> None:
        self.TICKER_MODEL_PATH = self.TICKER_MODEL_PATH + extended_model_path
        self.excluded = excluded
        self.NSETICKERS = [
            ticker for ticker in self.NSETICKERS if ticker not in self.excluded]

    def stock_movement(self, days: int) -> dict:
        '''
        Returns the stock movement of the last 5 days
        '''
        stock_movement = {}
        hd = HistoricalData()
        data = hd.get_recent_data()
        for ticker in self.NSETICKERS:
            model = load_model(self.TICKER_MODEL_PATH+f'{ticker}.h5')
            sp = StockPrediction(model, data[ticker])
            results = sp.long_prediction(days).flatten()
            dict1 = {"days": days,
                     "prediction": results[-1],
                     "profit/loss": "profit" if results[-1] > results[0] else "loss",
                     "diff": results[-1] - results[0],
                     "percentage": (results[-1] - results[0])/results[0] * 100,
                     }
            stock_movement[ticker] = dict1
        return stock_movement

    def generate(self) -> dict:
        result = {x: self.stock_movement(x) for x in range(1, 7)}
        return result
        
if __name__ == '__main__':
    bs = BestStocks(extended_model_path='models_221211/')
    print(bs.generate())

            