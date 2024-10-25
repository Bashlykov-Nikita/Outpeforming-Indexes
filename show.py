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


# TODO: Del index arg
def show_growth_plot(bt: pd.Series, selected_index) -> None:
    bt_df = pd.DataFrame({"Timeline": bt.index, "Return": (1 + bt.values).cumprod()})
    # bt_df[f"{selected_index}"] = get.get_index_returns_for_comp(selected_index).values
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
    bt_df = pd.DataFrame({"Date": bt.index, "Returns": bt.values})
    # fig = px.histogram(bt_df["Returns"], histnorm="probability", marginal="box")
    # fig = ff.create_distplot(
    #     [bt_df["Returns"]],
    #     ["Returns"],
    #     show_hist=False,
    # )
    fig = px.histogram(
        bt_df["Returns"],
        x="Returns",
        histnorm="probability",
        title="Probability distribution:",
        # marginal="rug",
    )
    st.write(fig)


def show_portfolios_plots(
    weights: pd.Series, backtest: pd.Series, index_name: str
) -> None:
    growth, top_weights, risc_contribution = st.columns(3, gap="Small")
    with growth:
        show_growth_plot(backtest, index_name)
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


#! One show growth
# ? Outperfom Plots
def show_comparative_growth_plot(bt: pd.DataFrame, selected_index) -> None:

    bt[f"{selected_index}"] = get.get_index_returns_for_comp(
        selected_index, bt.index.min(), bt.index.max()
    ).values
    fig = px.line(
        (1 + bt).cumprod(), x=bt.index, y=list(bt.columns), title="Growth Plot:"
    )
    st.write(fig)


def show_comparative_summary_stats(all_portfolios_bt: pd.DataFrame) -> pd.DataFrame:
    # all_stats_df = pd.DataFrame()
    # for col in all_portfolios_bt:
    #     stats = c.summary_stats(all_portfolios_bt[col])
    #     all_stats_df = all_stats_df._append(stats)
    st.table(u.table_highlight(get.get_all_stats(all_portfolios_bt)))


#! Unify in one functon:
def show_var_cvar_mdd_comp(stats: pd.DataFrame) -> None:
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
            color=stats["Max Drawdown"],
            color_continuous_scale=colors,
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        for axis in fig.layout:
            if axis.startswith("yaxis"):
                fig.layout[axis].title = ""
        st.write(fig)
