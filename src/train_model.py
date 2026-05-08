from prophet import Prophet

def train_model(df):

    train_size = int(len(df) * 0.8)

    train = df[:train_size]
    test = df[train_size:]

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        seasonality_mode='multiplicative'
    )

    # IMPORTANT: add temperature
    model.add_regressor('temperature_c')

    model.fit(train)

    future = model.make_future_dataframe(periods=len(test), freq='D')

    future = future.merge(df[['ds', 'temperature_c']], on='ds', how='left')

    forecast = model.predict(future)

    return forecast, test