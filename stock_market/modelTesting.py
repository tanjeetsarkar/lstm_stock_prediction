from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import datetime


class PmTesting():
    '''
    Testing the model created using Model Creation
    '''

    def __init__(self, model, data, timestep: int = 60) -> None:
        self.model = model
        self.data = data
        self.timestep = timestep
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def test_model(self):
        '''
        Testing the model
        '''
        test_set = self.data.iloc[:, 4:5].values
        test_set = self.scaler.fit_transform(test_set)
        X_test = []
        y_test = []
        for i in range(self.timestep, len(test_set)):
            X_test.append(test_set[i-self.timestep:i, 0])
            y_test.append(test_set[i, 0])
        X_test, y_test = np.array(X_test), np.array(y_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        predicted_stock_price = self.model.predict(X_test)
        predicted_stock_price = self.scaler.inverse_transform(
            predicted_stock_price)
        return predicted_stock_price

    def model_accuracy(self, predicted_stock_price):
        '''
        Calculating the accuracy of the model
        '''
        test_set = self.data.iloc[:, 4:5].values
        test_set = test_set[self.timestep:, :]
        accuracy = 0
        for i in range(len(predicted_stock_price)):
            accuracy += abs(
                (predicted_stock_price[i] - test_set[i])/test_set[i])
        accuracy = (1 - accuracy/len(predicted_stock_price))*100
        return accuracy


if __name__ == '__main__':
    data = pd.read_csv('SBIN.NS.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data = data[data['Date'] > datetime.datetime(2022, 1, 1)]
    model = load_model(f'test_model.h5')
    pmt = PmTesting(model, data)
    predicted_stock_price = pmt.test_model()
    print(predicted_stock_price)
    accuracy = pmt.model_accuracy(predicted_stock_price)
    print(accuracy)
