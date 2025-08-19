import pandas as pd
import time
from sqlalchemy import create_engine
from GetBitcoin import get_bitcoin_data_frame
from GetCommodities import get_commodities_data_frame

from dotenv import load_dotenv
import os

load_dotenv()

#CONFIGURAÇÃO DO BANCO DE DADOS
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

#CRIAR CONEXÃO COM SQLALCHEMY
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
engine = create_engine(DATABASE_URL)

SLEEP_SECONDS = 60  # Intervalo de tempo entre as atualizações

if __name__ == "__main__":
    while True:
        #COLETAR DADOS
        df_btc = get_bitcoin_data_frame()
        df_commodities = get_commodities_data_frame()

        #JUNTA TODOS OS DATAFRAMES
        df = pd.concat([df_btc, df_commodities], ignore_index=True)

        #SALVAR NO BANCO DE DADOS
        df.to_sql('cotacoes', engine, if_exists='append', index=False)

        print('✅ Cotações inseridas com sucesso!')

        #ESPERA O PROXIMO LOOP
        time.sleep(SLEEP_SECONDS)