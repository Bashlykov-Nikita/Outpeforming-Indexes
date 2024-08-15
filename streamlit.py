import streamlit as st
import numpy as np
import pandas as pd
import main as m
import calc as c
import time

st.title("Outperforming Indexes")
st.markdown(" Data from Yahoo Finance ")

with st.sidebar:

    st.title("Options")

    select_index = st.selectbox(
        "Choose Index",
        (
            "S&P 500",
            "Nasdaq Composite",
            "Dow Jones Industrial Average",
            "Russell 2000",
            "FTSE 100",
            "DAX PERFORMANCE-INDEX",
            "CAC 40",
            "Nikkei 225",
            "HANG SENG INDEX",
        ),
    )

    select_cov = st.selectbox(
        "Select Covariance", ("Sample", "Elton-Gruber", "Shinkage")
    )


def show_stats(index_data):
    c.summary_stats(pd.DataFrame(m.resample_data(index_data)))


match select_index:
    case "S&P 500":

        # @st.cache_data
        def show_sp500():
            index_name = "^GSPC"
            st.write("S&P 500 historical data:")
            st.write(m.fetch_index_data(index_name))
            # st.write(show_stats(m.fetch_index_data(index_name)))
            st.write(
                c.summary_stats(
                    pd.DataFrame(m.resample_data(m.fetch_index_data(index_name)))
                )
            )

        show_sp500()
    case "Nasdaq Composite":

        @st.cache_data
        def show_NC():
            index_name = "^IXIC"
            st.write("Nasdaq Composite historical data:")
            st.write(m.fetch_index_data(index_name))

        show_NC()
    case "Dow Jones Industrial Average":

        @st.cache_data
        def show_DJI():
            index_name = "^DJI"
            st.write("Dow Jones Industrial Average historical data:")
            st.write(m.fetch_index_data(index_name))

        show_DJI()
    case "Russell 2000":

        @st.cache_data
        def show_RUT():
            index_name = "^RUT"
            st.write("Russell 2000 historical data:")
            st.write(m.fetch_index_data(index_name))

        show_RUT()
    case "FTSE 100":

        @st.cache_data
        def show_FTSE():
            index_name = "^FTSE"
            st.write("FTSE 100 historical data:")
            st.write(m.fetch_index_data(index_name))

        show_FTSE()
    case "DAX PERFORMANCE-INDEX":

        @st.cache_data
        def show_GDAXI():
            index_name = "^GDAXI"
            st.write("DAX PERFORMANCE-INDEX historical data:")
            st.write(m.fetch_index_data(index_name))

        show_GDAXI()
    case "CAC 40":

        @st.cache_data
        def show_FCHI():
            index_name = "^FCHI"
            st.write("CAC 40 historical data:")
            st.write(m.fetch_index_data(index_name))

        show_FCHI()
    case "Nikkei 225":

        @st.cache_data
        def show_N225():
            index_name = "^N225"
            st.write("Nikkei 225 historical data:")
            st.write(m.fetch_index_data(index_name))

        show_N225()
    case "HANG SENG INDEX":

        @st.cache_data
        def show_HSI():
            index_name = "^HSI"
            st.write("HANG SENG INDEX historical data:")
            st.write(m.fetch_index_data(index_name))

        show_HSI()

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
