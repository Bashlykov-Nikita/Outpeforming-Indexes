import sys

sys.dont_write_bytecode = True
import streamlit as st
import data as d
import calc as c
import utils as u
import get
import show

#! Streamlit page
# * Main streamlit page file

# ? Initialization of session state
if "select_index" not in st.session_state:
    st.session_state["select_index"] = "None"
if "select_cov" not in st.session_state:
    st.session_state["select_cov"] = "Sample"
if "select_er" not in st.session_state:
    st.session_state["select_er"] = "Average"

# ? Configuring page
st.set_page_config(
    page_title="Outperforming Indexes",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title(":chart: Outperforming the Indexes")
st.caption("_Data from Yahoo Finance_")

# ? Defining sidebar options:
with st.sidebar:
    st.title("Options")
    # ? Saving chosen options (index, cov, er) to session state:
    st.session_state.select_index = st.selectbox(
        label="Choose Index",
        options=u.add_none_to_list(list(d.INDEXES.keys())),
        index=(
            u.add_none_to_list(list(d.INDEXES.keys())).index(
                st.session_state["select_index"]
            )
        ),
    )

    st.session_state.select_cov = st.selectbox(
        label="Select Covariance",
        options=d.COV.keys(),
        index=(list(d.COV.keys()).index(st.session_state["select_cov"])),
    )
    st.session_state.select_er = st.selectbox(
        label="Select Expected Return",
        options=d.ER.keys(),
        index=(list(d.ER.keys()).index(st.session_state["select_er"])),
    )
selected_er = st.session_state.select_er
selected_cov = st.session_state.select_cov
selected_index = st.session_state.select_index
selected_portfolio_options = u.add_none_to_list(list(d.PORTFOLIOS_NAMES.keys())) + [
    "Outperform!"
]

if selected_index != "None":
    st.write(
        f"You chose to outperform :green[{selected_index}] with :orange[{selected_cov}] covariance and :orange[{selected_er}] expected return!"
    )

    selected_portfolio = st.selectbox(
        label="Select Portfolio",
        options=selected_portfolio_options,
    )
    all_portfolios_weights = get.get_all_portfolios(
        selected_index, selected_cov, selected_er
    )
    all_portfolios_backtest = get.get_all_portfolios(
        selected_index, selected_cov, selected_er, backtest=True
    )
    all_portfolios_stats = get.get_all_stats(all_portfolios_backtest)
    if selected_portfolio == "Outperform!":
        # *Shows comparative growth plots, risk-return profiles,
        # * and summary statistics if "Outperform!" is selected.
        show.show_comparative_growth_plot(all_portfolios_backtest, selected_index)
        show.show_frontier_sharpe(all_portfolios_stats)
        show.show_var_cvar_mdd_comp(all_portfolios_stats)
        show.show_comparative_summary_stats(all_portfolios_backtest)
        st.write("Summary")

    elif selected_portfolio != "None":
        # * Displays specific portfolio statistics and plots if another portfolio is selected.
        try:
            chosen_portfolio_weights = get.get_certain_portfolio(
                all_portfolios_weights, selected_portfolio
            )
            chosen_portfolio_backtest = get.get_certain_portfolio(
                all_portfolios_backtest, selected_portfolio
            )
            portfolio_stats = c.summary_stats(chosen_portfolio_backtest)
            show.show_stats(portfolio_stats)
            show.show_portfolios_plots(
                chosen_portfolio_weights, chosen_portfolio_backtest
            )
        except Exception as e:
            st.error(
                f"Error fetching data for portfolio :red[{selected_portfolio}]. Error: {e}"
            )
