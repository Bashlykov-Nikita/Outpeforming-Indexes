import sys

sys.dont_write_bytecode = True
import pandas as pd
import yfinance as yf
import data as d
import calc as c
import utils as u

# * File with get functions


def get_df(url: str) -> pd.DataFrame:
    """Reads a CSV file from the specified URL and returns a DataFrame.

    Args:
        url (str): The URL of the CSV file to read.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(url, index_col=0)


def get_index_data(index_name: str, just_returns=False) -> pd.DataFrame:
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
        index_data["Return"] = c.calculate_return(index_data)
        index_data = index_data.dropna()

        if just_returns:
            return index_data["Return"]
        else:
            index_data.index = index_data.index.to_period("D")
            return index_data
    except Exception as e:
        print(f"Error fetching data for index: {index_name}. Error: {e}")
        return None


def get_index_returns_for_comp(selected_index: str) -> pd.DataFrame:
    return (
        1
        + u.resample_data(get_index_data(d.INDEXES[selected_index]))["Return"][
            "2020-01":
        ]
    ).cumprod()


def get_all_portfolios(
    index_name: str, cov: str, er: str, backtest=False
) -> pd.DataFrame:
    """Retrieve all portfolios based on the given index, covariance, and expected return.

    Args:
        index_name (str): Name of the index.
        cov (str): Type of covariance.
        er (str): Expected return type.
        backtest (bool, optional): Flag to indicate backtesting. Defaults to False.

    Returns:
        pd.DataFrame: DataFrame containing portfolios data.
    """
    cov_short = d.COV[cov]
    er_short = d.ER[er]
    portfolios_names_arr = [
        f"MSR_{cov_short}_{er_short}",
        f"GMV_{cov_short}",
        "EW",
        "CW",
        f"ERC_{cov_short}",
    ]
    if backtest:
        # ? CW currently not available
        without_cw = portfolios_names_arr[:3] + portfolios_names_arr[4:]
        return get_df(d.BACKTEST[index_name])[without_cw]
    else:
        return get_df(d.PORTFOLIOS_WEIGHTS[index_name])[portfolios_names_arr]


def get_certain_portfolio(
    all_portfolios: pd.DataFrame, portfolio_name: str
) -> pd.DataFrame:
    """
    Get a specific portfolio from a DataFrame based on the portfolio name prefix.

    Args:
        all_portfolios (pd.DataFrame): DataFrame containing portfolios data.
        portfolio_name (str): Name of the portfolio to retrieve.

    Returns:
        pd.DataFrame: DataFrame with the data of the specified portfolio.
    """
    prefix = d.PORTFOLIOS_NAMES[portfolio_name]
    for col in all_portfolios.columns:
        if col.startswith(prefix):
            return all_portfolios[col]
    return None
