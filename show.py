import sys

sys.dont_write_bytecode = True
import pandas as pd
import streamlit as st
import main as m
import calc as c
import data as d

# @st.cache_data


def show_index_historical_data(name):
    st.write(m.fetch_index_data(name))


# @st.cache_data
def show_stats(name):
    # TODO: if resample
    m_ind_data = pd.DataFrame(m.resample_data(m.fetch_index_data(name))["Return"])
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
    st.line_chart(data=(1 + m.fetch_index_data(name, True)).cumprod(), y="Return")


# TODO: One show function for index


def show_index_data(index_name: str):
    if index_name == "None":
        # TODO: Starting Page
        st.write("Choose Index")
    else:
        index_short_name = d.INDEXES[index_name]
        st.write(f"{index_name} historical data:")
        show_index_historical_data(index_short_name)
        show_stats(index_short_name)
        growth_plot(index_short_name)
