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
st.markdown(" Data from Yahoo Finance ")

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

# show.show_index_data(select_index)
selected_portfolio = st.selectbox(
    label="Select Portfolio",
    options=u.add_none_to_list(list(d.PORTFOLIOS_NAMES.keys())),
)


if selected_index != "None" and selected_portfolio != "None":
    all_portfolios_weights = get.get_all_portfolios(
        selected_index, selected_cov, selected_er
    )
    all_portfolios_backtest = get.get_all_portfolios(
        selected_index, selected_cov, selected_er, backtest=True
    )
    chosen_portfolio = get.get_certain_portfolio(
        all_portfolios_backtest, selected_portfolio
    )
    portfolio_stats = c.summary_stats(chosen_portfolio)

    # show.show_df(all_portfolios)
    # show.show_df(get.get_certain_portfolio(all_portfolios, selected_portfolio))
#     weights = m.get_certain_portfolio(selected_index, chosen_portfolio)[0]
#     backtest = m.get_certain_portfolio(selected_index, chosen_portfolio)[1]

#     total1, total2, total3, total4, total5 = st.columns(5, gap="small")
#     with total1:
#         st.info("Sum Investment", icon="💰")
#         st.metric(label="Sum TZS", value=f"{1:,.0f}")

#     with total2:
#         st.info("Most Investment", icon="💰")
#         st.metric(label="Mode TZS", value=f"{2:,.0f}")

#     with total3:
#         st.info("Average", icon="💰")
#         st.metric(label="Average TZS", value=f"{3:,.0f}")

#     with total4:
#         st.info("Central Earnings", icon="💰")
#         st.metric(label="Median TZS", value=f"{4:,.0f}")

#     with total5:
#         st.info("Ratings", icon="💰")
#         st.metric(label="Rating", value=5, help=f""" Total Rating: {5} """)
