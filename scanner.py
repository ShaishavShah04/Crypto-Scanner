"""
Functions File
Made by: Shaishav Shah
"""

def get_tickers(market, base = "BUSD"):
    busd = []
    # Getting all symbols
    for info in market:
        if info.get("quote") == base:
            busd.append(info.get("symbol"))
    return busd


def explosive_volume(df_volume):
    return df_volume.iloc[-1] > ( df_volume.iloc[-2] * 2 )


def bullish_engulfing(ticker_info, openPrice, closePrice):
    # Checking if last day was down
    if (closePrice < openPrice):
        price = ( ticker_info["ask"] + ticker_info["bid"] ) / 2
        if  price > openPrice:
            return True
    return False

def bearish_engulfing(ticker_info, openPrice, closePrice):
    # Checking if last day was up
    if (closePrice > openPrice):
        price = ( ticker_info["ask"] + ticker_info["bid"] ) / 2
        if  price < openPrice:
            return True
    return False


def price_level(ticker_info, openPrice, closePrice):
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


def analyze(ticker_info, df):
    # Some Basic things we need
        try:
          openPrice = df.iloc[-2]["open"]
          closePrice = df.iloc[-2]["close"]
          # Criteria
          price_up = (price_level(ticker_info, openPrice, closePrice) == "Up")
          higher_volume = explosive_volume(df["volume"])
          bullish_engulfing_check = bullish_engulfing(ticker_info, openPrice, closePrice)
          bearish_engulfing_check = bearish_engulfing(ticker_info, openPrice, closePrice)
        except IndexError:
            print("-- Not enough data. Probably a new listing!")
            return 0            
        if higher_volume and (bullish_engulfing_check or price_up):
            return 1
        elif higher_volume and bearish_engulfing_check:
            return -1
        else:
            return 0