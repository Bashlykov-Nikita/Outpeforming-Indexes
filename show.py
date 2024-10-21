import sys

sys.dont_write_bytecode = True
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
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
) -> None:
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


def show_stats(portfolio_stats: pd.DataFrame) -> None:
    columns_list = st.columns(len(portfolio_stats.columns), gap="small")
    for col, i in zip(columns_list, portfolio_stats.columns):
        with col:
            st.metric(
                label=i,
                value=f"{portfolio_stats[i].values[0]:.4f}",
                help=f"{d.HELP[i]}",
            )


def show_growth_plot(bt: pd.Series) -> None:
    bt_df = pd.DataFrame({"Timeline": bt.index, "Return": (1 + bt.values).cumprod()})
    # st.write("Growth plot:")
    # st.line_chart(data=(1 + bt).cumprod())
    fig = px.line(bt_df, x="Timeline", y="Return", title="Growth Plot:")
    st.write(fig)


def show_bar_chart(w: pd.Series) -> None:
    w = w.sort_values(ascending=True)
    top_w = (
        pd.DataFrame({"Companies": w.index, "Weights": w.values})
        .replace(0, np.NaN)
        .dropna()
        .drop_duplicates("Companies")
    )
    fig = px.bar(top_w, x="Weights", y="Companies", title="Top Weights:")
    st.write(fig)
    # st.write(top_w)


def show_dist_plot(bt: pd.Series) -> None:
    fig = px.histogram(bt.values)
    st.write(fig)


def show_portfolios_plots(weights: pd.Series, backtest: pd.Series) -> None:
    growth, top_weights, risc_contribution = st.columns(3, gap="Small")
    with growth:
        show_growth_plot(backtest)
    with top_weights:
        # show_df(weights)
        show_bar_chart(weights)
    with risc_contribution:
        show_dist_plot(backtest)


# @st.cache_data
# ! Not used
# ! Remake for new UI:


def show_index_data(index_name: str):
    if index_name == "None":
        # TODO: Starting Page
        st.write("Choose Index")
    else:
        index_short_name = d.INDEXES[index_name]
        show_stats(index_short_name)
        show_growth_plot(index_short_name)
