import sys

sys.dont_write_bytecode = True
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
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


# ? Show functions for data showcase page:
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


# ? Show functions for Outperform (selected portfolio) page:
def show_stats(portfolio_stats: pd.DataFrame) -> None:
    """
    Display statistics (in st.metric format) for the given portfolio.

    Args:
        portfolio_stats (pd.DataFrame): DataFrame containing portfolio statistics.
    """
    columns_list = st.columns(len(portfolio_stats.columns), gap="small")
    for col, i in zip(columns_list, portfolio_stats.columns):
        with col:
            st.metric(
                label=i,
                value=f"{portfolio_stats[i].values[0]:.4f}",
                help=f"{d.HELP[i]}",
            )


# TODO: Del index arg
def show_growth_plot(bt: pd.Series) -> None:
    """Generate a growth plot based on the input time series data.

    Args:
        bt (pd.Series): A pandas Series containing the historical returns for plotting.
    """
    bt_df = pd.DataFrame({"Timeline": bt.index, "Return": (1 + bt.values).cumprod()})
    fig = px.line(bt_df, x="Timeline", y="Return", title="Growth Plot:")
    st.write(fig)


def show_bar_chart(w: pd.Series) -> None:
    """Sorts the input pandas Series in ascending order, filters out zero values,
    removes duplicates, and displays a bar chart of the top weights for companies.

    Args:
        w (pd.Series): The pandas Series containing weights for companies.
    """
    w = w.sort_values(ascending=True)
    top_w = (
        pd.DataFrame({"Companies": w.index, "Weights": w.values})
        .replace(0, np.NaN)
        .dropna()
        .drop_duplicates("Companies")
    )
    fig = px.bar(top_w, x="Weights", y="Companies", title="Top Weights:")
    st.write(fig)


def show_dist_plot(bt: pd.Series) -> None:
    """Generate a probability distribution plot for a given time series.

    Args:
        bt (pd.Series): Time series data to plot the distribution for.
    """
    bt_df = pd.DataFrame({"Date": bt.index, "Returns": bt.values})
    fig = px.histogram(
        bt_df["Returns"],
        x="Returns",
        histnorm="probability",
        title="Probability distribution:",
        marginal="box",
    )
    st.write(fig)


def show_portfolios_plots(weights: pd.Series, backtest: pd.Series) -> None:
    """Displays growth, top weights, and risk contribution plots for portfolios.

    Args:
        weights (pd.Series): Pandas Series of weights for companies.
        backtest (pd.Series): Pandas Series of historical returns for plotting.
    """
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

#! One show growth


# ? Show functions for Outperform! page:
def show_comparative_growth_plot(bt: pd.DataFrame, selected_index) -> None:
    """
    Plots the comparative growth of a specified index against a Porfolios.

    Args:
        bt (pd.DataFrame): DataFrame with portfolios backtest.
        selected_index (str): Name of the index for comparison.
    """
    bt[f"{selected_index}"] = get.get_index_returns_for_comp(
        selected_index, bt.index.min(), bt.index.max()
    ).values
    fig = px.line(
        (1 + bt).cumprod(), x=bt.index, y=list(bt.columns), title="Growth Plot:"
    )
    st.write(fig)


def show_frontier_sharpe(stats):
    """
    Display the Portfolio Risk-Return Profile and Sharpe Ratio for each portfolio.

    Args:
        stats (DataFrame): A DataFrame containing portfolio statistics including Return, Volatility, and Sharpe Ratio.
    """
    frontier, sharpe = st.columns(2, gap="Small")
    with frontier:
        frontier = pd.DataFrame(
            {
                "Portfolio": stats.index,
                "Return": stats["Return"],
                "Volatility": stats["Volatility"],
            }
        )
        fig = px.scatter(
            frontier,
            x="Volatility",
            y="Return",
            color="Portfolio",
            hover_name="Portfolio",
            hover_data=["Return", "Volatility"],
        )

        fig.update_layout(title="Portfolio Risk-Return Profile:")

        st.write(fig)
    with sharpe:
        sharpe = pd.DataFrame(
            {"Portfolio": stats.index, "Sharpe Ratio": stats["Sharpe Ratio"]}
        )
        fig = px.bar(
            sharpe,
            x="Portfolio",
            y="Sharpe Ratio",
            color="Portfolio",
            hover_name="Portfolio",
        )
        fig.update_layout(title="Sharpe Ratio:")
        for axis in fig.layout:
            if axis.startswith("xaxis"):
                fig.layout[axis].title = ""
        st.write(fig)


#! Unify in one functon:
def show_var_cvar_mdd_comp(stats: pd.DataFrame) -> None:
    """Display bar charts for VaR, CVaR, and Max Drawdown.

    Args:
        stats (pd.DataFrame): DataFrame containing statistics data.
    """
    var, cvar, mdd = st.columns(3, gap="Small")
    with var:
        colors = px.colors.sequential.Viridis[: len(stats)]
        fig = px.bar(
            stats,
            x="VaR (5%)",
            title="VaR (5%):",
            color=stats["VaR (5%)"],
            color_continuous_scale=colors,
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        for axis in fig.layout:
            if axis.startswith("yaxis"):
                fig.layout[axis].title = ""
        st.write(fig)
    with cvar:
        colors = px.colors.sequential.Sunset[: len(stats)]
        fig = px.bar(
            stats,
            x="CVaR (5%)",
            title="CVaR (5%):",
            color=stats["CVaR (5%)"],
            color_continuous_scale=colors,
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        for axis in fig.layout:
            if axis.startswith("yaxis"):
                fig.layout[axis].title = ""
        st.write(fig)
    with mdd:
        colors = px.colors.sequential.Bluered[: len(stats)]
        fig = px.bar(
            abs(stats),
            x="Max Drawdown",
            title="Max Drawdown:",
            color="Max Drawdown",
            color_continuous_scale=colors,
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        for axis in fig.layout:
            if axis.startswith("yaxis"):
                fig.layout[axis].title = ""
        st.write(fig)


def show_comparative_summary_stats(all_portfolios_bt: pd.DataFrame) -> None:
    """
    Display a comparative summary of statistics for all portfolios.

    Args:
        all_portfolios_bt (pd.DataFrame): DataFrame containing portfolios' backtest.
    """
    st.table(u.table_highlight(get.get_all_stats(all_portfolios_bt)))
