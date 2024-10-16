import sys

sys.dont_write_bytecode = True
import pandas as pd
import streamlit as st
import utils as u
import calc as c
import data as d
import get

# * File with show functions


# @st.cache_data
def show_df(df: pd.DataFrame) -> None:
    """Shows DataFrame on Streamlit app

    Args:
        df (pd.DataFrame): DataFrame you want to show
    """
    st.write(df)


def show_index_hist_data(short_name: str) -> None:
    """Shows index historical data

    Args:
        short_name (str): Index short name
    """
    show_df(get.get_index_data(short_name))


def show_portfolios_weights_and_backtest(
    index_name: str, cov: str, er: str, backtest=False
):
    """Shows portfolios weights or backtest if specified.

    Args:
        index_name (str): Name of the index.
        cov (str): Type of covariance.
        er (str): Expected return type.
        backtest (bool, optional): Flag to indicate backtesting. Defaults to False.
    """
    if backtest:
        show_df(get.get_all_portfolios(index_name, cov, er, backtest=True))
    else:
        show_df(get.get_all_portfolios(index_name, cov, er))


# @st.cache_data
# ! Not used
# ! Remake for new UI:
# TODO: Make general show_stats function
def show_index_stats(name, resample):
    # TODO: if resample
    m_ind_data = pd.DataFrame(u.resample_data(get.get_index_data(name))["Return"])
    stats_df = c.summary_stats(m_ind_data)
    st.write(
        stats_df[
            ["Annualized Return", "Annualized Vol", "Sharpe Ratio", "Max Drawdown"]
        ]
    )
    st.write(
        stats_df[
            ["Skewness", "Kurtosis", "Cornish-Fisher VaR (5%)", "Historic CVaR (5%)"]
        ]
    )


def show_growth_plot(name):
    st.line_chart(data=(1 + get.get_index_data(name, True)).cumprod(), y="Return")


def show_index_data(index_name: str):
    if index_name == "None":
        # TODO: Starting Page
        st.write("Choose Index")
    else:
        index_short_name = d.INDEXES[index_name]
        show_stats(index_short_name)
        show_growth_plot(index_short_name)
