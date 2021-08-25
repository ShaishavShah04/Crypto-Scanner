"""
Cypto Scanner - Main File
-- Hoping to catch all those midnight 200% surges
Made by: Shaishav Shah
"""

import ccxt
from pprint import pprint as pp
import scanner
import pandas as pd

# Exchange
exchange = ccxt.binance({
    'enableRateLimit': True,
})

# Init Variables Needed
def check_cypto_market(timeframe = "4h"):
    crypto_to_watch = set()
    market = exchange.fetch_markets()
    symbols = scanner.get_tickers( market, base="BUSD" )
    filtered = []
    all_tickers = exchange.fetch_tickers()

    for symbol in symbols:
        print(f"Testing {symbol}...")
        # Fetching Data
        df = pd.DataFrame( exchange.fetch_ohlcv(symbol,timeframe, limit=3), columns = ["time", "open", "high", "low", "close", "volume"] )
        ticker_info = all_tickers.get(symbol)
        signal = scanner.analyze(ticker_info, df)
        # Processing Singal
        if signal:
            if signal == -1:
                crypto_to_watch.discard(symbol)
            else:
                crypto_to_watch.add(symbol)
        

    print(crypto_to_watch)



check_cypto_market()