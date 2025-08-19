import pandas as pd
import time
from GetBitcoin import get_bitcoin_data_frame
from GetCommodities import get_commodities_data_frame


while True:

    valor_bitcoin = get_bitcoin_data_frame()
    valor_commodities = get_commodities_data_frame()

    df = pd.concat([valor_bitcoin, valor_commodities], ignore_index=True)
    print(df)

    time.sleep(60) # Espera por 60 segundos antes de atualizar os dados