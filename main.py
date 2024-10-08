import numpy as np
import pandas as pd
import yfinance as yf

import calc as c


def calculate_return(data):
    """
    Calculate the return on an investment based on the given data.

    Parameters:
    - data (pandas.DataFrame): A DataFrame containing at least "Open" and "Close" columns.

    Returns:
    - pandas.Series: A Series representing the calculated returns.
    """
    return (data["Close"] - data["Open"]) / data["Open"]


def fetch_index_data(index_name, just_returns=False):
    """
    Fetches historical data for a specified index.

    Parameters:
    - index_name (str): Name of the index to fetch data for.
    - just_returns (bool, optional): If True, returns only the calculated returns.
    If False, returns the complete historical data with calculated returns.

    Returns:
    - pandas.DataFrame or pandas.Series: Historical data for the index with calculated returns,
    or just the calculated returns if 'just_returns' is True. Returns None if an error occurs during data fetching.
    """
    try:
        index_data = yf.Ticker(index_name)
        index_data = index_data.history(period="max")
        index_data.drop(columns=["Dividends", "Stock Splits"], inplace=True)
        index_data = index_data.loc[index_data["Open"] != 0]
        index_data["Return"] = calculate_return(index_data)
        index_data = index_data.dropna()

        if just_returns:
            return index_data["Return"]
        else:
            index_data.index = index_data.index.to_period("D")
            return index_data
    except Exception as e:
        print(f"Error fetching data for index: {index_name}. Error: {e}")
        return None


def resample_data(index_data):
    """
    Resamples the input index data to monthly frequency by compounding the returns and converting the data to monthly periods.
    """
    index_data = index_data.to_timestamp()
    index_data_m = index_data.resample("M").apply(c.compound).to_period("M")
    return index_data_m
