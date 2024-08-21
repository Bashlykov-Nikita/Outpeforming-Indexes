import numpy as np
import pandas as pd
import yfinance as yf

import calc as c


# TODO: Unify
def data_for_plots(index_name):
    index_data = yf.Ticker(index_name)
    index_data = index_data.history(period="max")
    mask = index_data["Open"] == 0
    index_data = index_data[~mask]
    index_data["Return"] = (index_data["Close"] - index_data["Open"]) / index_data[
        "Open"
    ]
    return index_data["Return"]


def fetch_index_data(index_name):
    index_data = yf.Ticker(index_name)

    index_data = index_data.history(period="max")
    # del index_data["Dividends"]
    # del index_data["Stock Splits"]
    index_data.index = index_data.index.to_period("D")
    mask = index_data["Open"] == 0
    index_data = index_data[~mask]
    index_data["Return"] = (index_data["Close"] - index_data["Open"]) / index_data[
        "Open"
    ]
    index_data = index_data.dropna()
    return index_data


def resample_data(index_data):
    index_data = index_data.to_timestamp()
    index_data_m = index_data.resample("M").apply(c.compound).to_period("M")
    return index_data_m


def get_components(url):
    if url:
        return pd.read_csv(url)["Symbol"]
    else:
        return "Components data is not available yet :("


# Calculating all the history returns for all companies


def companies_returns_df(companies):
    tickers = companies
    first_ticker_data = yf.download(companies[0], period="max")
    # Create an empty DataFrame with a single row
    companies_df = pd.DataFrame(index=first_ticker_data.index, columns=tickers)

    # Fetch historical data for each ticker and populate the DataFrame
    for ticker in tickers:
        try:
            data = yf.download(ticker, period="max")
            if data.empty:
                companies_df[ticker] = 0
            else:
                data["Return"] = (data["Close"] - data["Open"]) / data["Open"]
                companies_df[ticker] = data["Return"]
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            companies_df[ticker] = (
                None  # Or handle the error differently, e.g., fill with 0
            )
    return companies_df
