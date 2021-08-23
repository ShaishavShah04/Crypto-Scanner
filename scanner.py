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

def bullish_engulfing(df, ticker_info):
    # Last High / Open
    openPrice = df.iloc[-2]["open"]
    closePrice = df.iloc[-2]["close"]
    # Checking if last day was down
    if (closePrice < openPrice):
        price = ( ticker_info["ask"] + ticker_info["bid"] ) / 2
        if  price > openPrice:
            return True
    return False

def price_level(df, ticker_info):
    
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
        ticker_info = exchange.fetch_tickers(symbol)[symbol]
        # Criteria
        upward_trend = (price_level(df, ticker_info) == "Up") and explosive_volume(df["volume"])
        bullish_engulfing_check = bullish_engulfing(df, ticker_info)

        if upward_trend or bullish_engulfing_check:
            filtered.append(symbol)
    
    print(filtered)

generate_bullish()
