import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_data_frame():
    # URL for the Coinbase API to get the current spot price of Bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"

    #Requesting the current spot price of Bitcoin
    response = requests.get(url)
    data = response.json()

    # Extracting the price from the JSON response
    preco = float(data['data']['amount'])
    ativo = data['data']['base']
    moeda = data['data']['currency']
    horario_de_coleta = datetime.now()

    data_frame = pd.DataFrame([{
        'ativo': ativo,
        'moeda': moeda,
        'preco': preco,
        'horario_de_coleta': horario_de_coleta
    }])
    
    return data_frame
