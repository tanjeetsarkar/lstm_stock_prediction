from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd


class StockPrediction():

    def __init__(self, model, data, timestep: int = 60):
        self.model = model
        self.data = data
        self.timestep = timestep
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def predict(self, data):
        if not self.check_unit_data_shape(data):
            raise ValueError('data should be in shape of (1, timestep, 1)')
        prediction = self.model.predict(data)
        return prediction

    def check_unit_data_shape(self, data) -> bool:
        '''Check the shape of the data'''
        return data.shape == (1, self.timestep, 1)

    def weekly_prediction(self, data: np.ndarray):
        '''data should be scaled and in shape of (1, timestep, 1)
        get predicition by appending prediciton to the data for 5 days'''
        prediction = []
        for i in range(5):
            pred = self.predict(data)
            prediction.append(self.unscale(pred))
            data = np.append(data, pred)
            data = data[1:]
            data = data.reshape(1, self.timestep, 1)
        return prediction

    def unscale(self, data):
        '''
        Unscale the data
        '''
        return self.scaler.inverse_transform(data)

    def continuous_weekly_prediction(self):
        '''
        data would be in shape of (len(data), timestep, 1)
        '''
        w_data = self.data.iloc[:, 1:2].values
        w_data = self.scaler.fit_transform(w_data)
        w_test = []
        for i in range(self.timestep, len(w_data)):
            w_test.append(w_data[i-self.timestep:i, 0])
        print("LENGTH OF W_TEST", len(w_test))
        w_data = np.reshape(np.array(w_test), (len(w_data), self.timestep, 1))
        w_result = [self.weekly_prediction(x)[-1] for x in w_data]

        return np.array(w_result)


if __name__ == '__main__':
    from tensorflow.keras.models import load_model
    model = load_model('sbi_model.h5')
    df = pd.read_csv('SBIN.NS.csv')
    df = df.dropna()
    train_ind = int(len(df)*0.8)
    df_test = df[train_ind:]
    print(len(df_test))
    sp = StockPrediction(model, df_test)
    w_result = sp.continuous_weekly_prediction()
