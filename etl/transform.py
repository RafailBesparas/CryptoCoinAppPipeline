import pandas as pd

def transform_data(df):
    print("Transforming the data for storage")

    # Select relevant columns
    df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'last_updated']]

    # Convert time to datetime format
    df['last_updated'] = pd.to_datetime(df['last_updated'])

    # Rename columns
    df.columns = ['coin_id', 'symbol', 'name', 'price_usd', 'market_cap', 'volume', 'timestamp']

    return df
