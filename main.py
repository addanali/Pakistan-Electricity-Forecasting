from src.preprocess import load_data
from src.train_model import train_model
from src.forecast import plot_all
from src.arima_model import train_arima

from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def main():

    # --------------------
    # LOAD DATA
    # --------------------
    df = load_data("data/pakistan_energy.csv")

    # --------------------
    # PROPHET MODEL
    # --------------------
    forecast, test = train_model(df)

    prophet_pred = forecast['yhat'][-len(test):].values
    actual = test['y'].values

    prophet_mae = mean_absolute_error(actual, prophet_pred)
    prophet_rmse = np.sqrt(mean_squared_error(actual, prophet_pred))

    print("\nPROPHET RESULTS:")
    print("MAE:", prophet_mae)
    print("RMSE:", prophet_rmse)

    # --------------------
    # ARIMA MODEL (ADD HERE)
    # --------------------
    arima_pred, arima_test = train_arima(df)

    arima_mae = mean_absolute_error(arima_test, arima_pred)
    arima_rmse = np.sqrt(mean_squared_error(arima_test, arima_pred))

    print("\nARIMA RESULTS:")
    print("MAE:", arima_mae)
    print("RMSE:", arima_rmse)

    # --------------------
    # PLOTS (PROPHET ONLY)
    # --------------------
    plot_all(forecast, test, df)

    # --------------------
    # FINAL COMPARISON
    # --------------------
    print("\nFINAL COMPARISON:")
    print("Prophet RMSE:", prophet_rmse)
    print("ARIMA RMSE:", arima_rmse)

if __name__ == "__main__":
    main()