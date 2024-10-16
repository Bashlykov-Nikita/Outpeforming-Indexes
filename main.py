import sys

sys.dont_write_bytecode = True
import numpy as np
import pandas as pd
import yfinance as yf
import data as d
import calc as c


def resample_data(index_data):
    """
    Resamples the input index data to monthly frequency by compounding the returns and converting the data to monthly periods.
    """
    index_data = index_data.to_timestamp()
    index_data_m = index_data.resample("M").apply(c.compound).to_period("M")
    return index_data_m


# def select_portfolio_name(portfolio_name: str, cov: str, er: str) -> pd.DataFrame:
#     portfolio_name_short = d.PORTFOLIOS_NAMES[portfolio_name]
#     cov_short = d.COV[cov]
#     er_short = d.ER[er]
#     portfolio = f"{portfolio_name_short}_{cov_short}_{er_short}"
#     return portfolio


# def get_certain_portfolio(index_name: str, portfolio_name: str):
#     portfolio_weights = d.get_df(d.PORTFOLIOS_WEIGHTS[index_name])[portfolio_name]
#     portfolio_backtest = d.get_df(d.BACKTEST[index_name])[portfolio_name]
#     return [portfolio_weights, portfolio_backtest]
