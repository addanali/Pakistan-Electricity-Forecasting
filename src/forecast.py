import matplotlib.pyplot as plt

def plot_all(forecast, test, df):

    # -------------------------------
    # GRAPH 1: Actual vs Predicted
    # -------------------------------
    plt.figure(figsize=(12,6))
    plt.plot(test['ds'], test['y'], label="Actual")
    plt.plot(test['ds'], forecast['yhat'][-len(test):], label="Predicted")
    plt.legend()
    plt.title("Actual vs Predicted")
    plt.savefig("outputs/graph_actual_vs_pred.png")
    plt.close()

    # -------------------------------
    # GRAPH 2: Future Forecast
    # -------------------------------
    plt.figure(figsize=(12,6))
    plt.plot(forecast['ds'], forecast['yhat'])
    plt.title("Future Forecast")
    plt.savefig("outputs/graph_future_forecast.png")
    plt.close()

    # -------------------------------
    # GRAPH 3: Monthly Trend
    # -------------------------------
    df['month'] = df['ds'].dt.month
    monthly = df.groupby('month')['y'].mean()

    plt.figure(figsize=(10,5))
    plt.plot(monthly.index, monthly.values, marker='o')
    plt.title("Monthly Trend")
    plt.savefig("outputs/graph_monthly_trend.png")
    plt.close()

    # -------------------------------
    # GRAPH 4: Temperature vs Usage
    # -------------------------------
    plt.figure(figsize=(10,5))
    plt.scatter(df['temperature_c'], df['y'])
    plt.title("Temperature vs Electricity")
    plt.savefig("outputs/graph_temp_vs_usage.png")
    plt.close()