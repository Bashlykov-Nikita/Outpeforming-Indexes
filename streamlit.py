import streamlit as st
import numpy as np
import pandas as pd
import main as m
import time

st.title("Outperforming Indexes")
st.markdown(" Data from Yahoo Finance ")

with st.sidebar:

    st.title("Options")

    select_index = st.selectbox("Choose Index", ("S&P 500", "Nasdaq Composite"))

    select_cov = st.selectbox(
        "Select Covariance", ("Sample", "Elton-Gruber", "Shinkage")
    )

if select_index == "S&P 500":
    index_name = "^GSPC"
    st.write("S&P 500 historical data:")

    @st.cache_data
    def show_sp500():
        st.write(m.fetch_index_data(index_name))

    show_sp500()

if select_index == "Nasdaq Composite":

    @st.cache_data
    def show_NC():
        index_name = "^IXIC"
        st.write("Nasdaq Composite historical data:")
        st.write(m.fetch_index_data(index_name))

    show_NC()
