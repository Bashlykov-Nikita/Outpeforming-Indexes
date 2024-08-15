import numpy as np
import pandas as pd
import yfinance as yf
import calc as c


def fetch_index_data(index_name):
    index_data = yf.Ticker(index_name)

    index_data = index_data.history(period="max")
    del index_data["Dividends"]
    del index_data["Stock Splits"]
    index_data.index = index_data.index.to_period("D")
    mask = index_data["Open"] == 0
    index_data = index_data[~mask]
    index_data["Return"] = (index_data["Close"] - index_data["Open"]) / index_data[
        "Open"
    ]
    index_data = index_data.dropna()
    return index_data


# sp500_index = data.sp500_index.to_timestamp()
# sp500_index_m = sp500_index.resample("M").apply(backtest.compound).to_period("M")
# TODO: Clear empty slots
def resample_data(index_data):
    index_data = index_data.to_timestamp()
    index_data_m = index_data.resample("M").apply(c.compound).to_period("M")
    return index_data_m["Return"]
