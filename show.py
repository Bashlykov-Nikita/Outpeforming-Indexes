import sys

sys.dont_write_bytecode = True
import pandas as pd
import streamlit as st
import main as m
import calc as c
import data as d
import get

# @st.cache_data


def show_df(df: pd.DataFrame):
    st.write(df)


def show_index_hist_data(short_name: str):
    st.write(get.get_index_data(short_name))


def show_portfolios_weights_and_backtest(
    index_name: str, cov: str, er: str, backtest=False
):
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
        show_df(get.get_df(d.BACKTEST[index_name])[without_cw])
    else:
        show_df(get.get_df(d.PORTFOLIOS_WEIGHTS[index_name])[portfolios_names_arr])


# @st.cache_data
def show_stats(name):
    # TODO: if resample
    m_ind_data = pd.DataFrame(m.resample_data(get.get_index_data(name))["Return"])
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


# @st.cache_data
def growth_plot(name):
    st.line_chart(data=(1 + get.get_index_data(name, True)).cumprod(), y="Return")


# TODO: One show function for index


def show_index_data(index_name: str):
    if index_name == "None":
        # TODO: Starting Page
        st.write("Choose Index")
    else:
        index_short_name = d.INDEXES[index_name]
        show_stats(index_short_name)
        growth_plot(index_short_name)
