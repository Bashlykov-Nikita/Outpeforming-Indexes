import numpy as np
import pandas as pd
import yfinance as yf


def fetch_index_data(index_name):
    sp500 = yf.Ticker(index_name)
    sp500 = sp500.history(period="max")
    del sp500["Dividends"]
    del sp500["Stock Splits"]
    sp500.index = sp500.index.to_period("D")
    sp500["Return"] = (sp500["Close"] - sp500["Open"]) / sp500["Open"]
    sp500 = sp500.dropna()
    return sp500
