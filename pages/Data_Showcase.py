import sys

sys.dont_write_bytecode = True
import streamlit as st
import data as d
import show


st.set_page_config(
    page_title="Outperforming Indexes",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.write("# :bar_chart: Used data")

selected_index = st.session_state["select_index"]
selected_cov = st.session_state["select_cov"]
selected_er = st.session_state["select_er"]
st.write(st.session_state["select_cov"])
st.write(st.session_state["select_er"])
st.write(st.session_state["select_index"])

st.write(f"#### {selected_index} historical data:")
show.show_index_hist_data(d.INDEXES[selected_index])

st.write("#### Recommended portfolios weights:")
st.write(f"With **{selected_cov}** covariance and **{selected_er}** expected return")
show.show_portfolios_weights_and_backtest(selected_index, selected_cov, selected_er)

st.write("#### Backtest data:")
show.show_portfolios_weights_and_backtest(
    selected_index, selected_cov, selected_er, backtest=True
)
