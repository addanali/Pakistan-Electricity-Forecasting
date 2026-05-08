import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df = df[['date', 'electricity_units_kwh', 'temperature_c']]

    df.rename(columns={
        'date': 'ds',
        'electricity_units_kwh': 'y'
    }, inplace=True)

    df['ds'] = pd.to_datetime(df['ds'])

    df = df.sort_values('ds')
    df = df.dropna()

    return df