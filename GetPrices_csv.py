import os
import time
import pandas as pd
from GetBitcoin import get_bitcoin_data_frame
from GetCommodities import get_commodities_data_frame

SLEEP_SECONDS = 60  # Intervalo de atualização em segundos
CSV_PATH = 'cotacoes.csv'

if __name__ == "__main__":
    if not os.path.exists(CSV_PATH):
        # escreve o cabeçalho do CSV se ele não existir
        cols = ['ativo', 'preco', 'moeda', 'horario_de_coleta']
        pd.DataFrame(columns=cols).to_csv(CSV_PATH, index=False)

    while True:
        #coleta os dados de Bitcoin e Commodities
        df_btc = get_bitcoin_data_frame()
        df_commodities = get_commodities_data_frame()

        #concatena os DataFrames
        df = pd.concat([df_btc, df_commodities], ignore_index=True)

        #salva os dados no CSV
        df.to_csv(CSV_PATH, mode='a', header=False, index=False)

        #espera por 60 segundos antes de atualizar os dados
        time.sleep(SLEEP_SECONDS)
