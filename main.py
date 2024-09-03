import numpy as np
import pandas as pd
import yfinance as yf

import calc as c


def fetch_index_data(index_name, just_returns=False):
    index_data = yf.Ticker(index_name)

    index_data = index_data.history(period="max")
    del index_data["Dividends"]
    del index_data["Stock Splits"]

    mask = index_data["Open"] == 0
    index_data = index_data[~mask]
    index_data["Return"] = (index_data["Close"] - index_data["Open"]) / index_data[
        "Open"
    ]
    index_data = index_data.dropna()
    if just_returns:
        return index_data["Return"]
    else:
        index_data.index = index_data.index.to_period("D")
        return index_data


def resample_data(index_data):
    index_data = index_data.to_timestamp()
    index_data_m = index_data.resample("M").apply(c.compound).to_period("M")
    return index_data_m


# Calculating all the history returns for all companies
