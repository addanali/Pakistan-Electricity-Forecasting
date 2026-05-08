from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_model(forecast, test):

    predicted = forecast['yhat'][-len(test):].values
    actual = test['y'].values

    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))

    print("\nModel Performance:")
    print("MAE:", mae)
    print("RMSE:", rmse)