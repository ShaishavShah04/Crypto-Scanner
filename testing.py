"""
Cypto Scanner
-- Hoping to catch all those midnight 200% surges
Made by: Shaishav Shah
"""
import ccxt, json
from pprint import pprint as pp
import ta
import pandas as pd


exchange = ccxt.binance()
data = exchange.load_markets()


def get_tickers( base = "BUSD" ):
    # Getting all symbols
    symbols = []
    for symbol in data:
        if symbol.split("/")[-1] == base:
            symbols.append(symbol)
    return symbols


df = pd.DataFrame( exchange.fetch_ohlcv("DOGE/BUSD","15m", limit=3),
                   columns = ["time", "open", "high", "low", "close", "volume"] )

pp(df)

print(df["volume"].iloc[-1])

def explosive_volume(df_volume):
    return df_volume.iloc[-1] > ( df_volume.iloc[-1] * 3 )
