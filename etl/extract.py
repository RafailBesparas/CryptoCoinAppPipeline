import requests
import pandas as pd

def extract_data():
    print("Extracting cryptocurrency data from CoinGecko API to create the Coinbase like monitor")

    # API Endpoint / Page where I will get the data
    url = "https://api.coingecko.com/api/v3/coins/markets"

    # Parameters that will assist me to get the data
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': 'false'
    }

    response = requests.get(url, params=params)
    
    # If the response is 200 which means success The client has requested documents from the server. 
    # The server has replied to the client and given the client the documents. All is well
    # Else we dont get any data
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")