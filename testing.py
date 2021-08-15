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

def get_tickers(data, base = "BUSD" ):
    # Getting all symbols
    symbols = []
    for symbol in data:
        if symbol.split("/")[-1] == base:
            symbols.append(symbol)
    return symbols

def explosive_volume(df_volume):
    return df_volume.iloc[-1] > ( df_volume.iloc[-2] * 2 )

def price_level(df, symbol):
    ticker_info = exchange.fetch_tickers(symbol)[symbol]
    # Last High / Open
    openPrice = df.iloc[-2]["open"]
    closePrice = df.iloc[-2]["close"]
    # 
    if closePrice > openPrice:
        previous_timeframe_peak = closePrice
        previous_timeframe_low = openPrice
    else:
        previous_timeframe_peak = openPrice
        previous_timeframe_low = closePrice
    # Comparing Current price to yesterdays price
    price = ( ticker_info["ask"] + ticker_info["bid"] ) / 2
    # Result
    if price > previous_timeframe_peak:
        return "Up"
    if price < previous_timeframe_low:
        return "Down"
    return price > previous_timeframe_peak

def generate_bullish():
    data = exchange.load_markets()
    symbols = get_tickers(data)
    filtered = []
    for symbol in symbols:
        print(f"Testing {symbol}...")
        df = pd.DataFrame( exchange.fetch_ohlcv(symbol,"1d", limit=3), columns = ["time", "open", "high", "low", "close", "volume"] )
        if explosive_volume(df["volume"]) and price_level(df, symbol) == "Up":
            filtered.append(symbol)
    
    print(filtered)
