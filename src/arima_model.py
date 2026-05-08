import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def train_arima(df):

    # Use only target variable
    series = df['y']

    train_size = int(len(series) * 0.8)
    train, test = series[:train_size], series[train_size:]

    # ARIMA model (simple config)
    model = ARIMA(train, order=(5,1,0))
    model_fit = model.fit()

    # Forecast
    forecast = model_fit.forecast(steps=len(test))

    return forecast, test