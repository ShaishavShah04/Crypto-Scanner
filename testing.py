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


df = pd.DataFrame( exchange.fetch_ohlcv("ADA/BUSD","1d", limit=3),
                   columns = ["time", "open", "high", "low", "close", "volume"] )

def explosive_volume(df_volume):
    return df_volume.iloc[-1] > ( df_volume.iloc[-1] * 3 )

def increasing_price(df, symbol):
    ticker_info = exchange.fetch_tickers(symbol)[symbol]
    # Last High / Open
    openPrice = df.iloc[-2]["open"]
    closePrice = df.iloc[-2]["close"]
    previous_timeframe_peak = closePrice if closePrice > openPrice else openPrice
    # Comparing Current price to yesterdays price
    price = ( ticker_info["ask"] + ticker_info["bid"] ) / 2
    # print(f"Open Price: {openPrice}")
    # print(f"Close Price: {closePrice}")
    # print(price)
    return price > previous_timeframe_peak


