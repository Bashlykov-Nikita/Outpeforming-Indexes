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


def show_index_historical_data(name):
    st.write(m.fetch_index_data(name))


def show_stats(name):
    stats_df = c.summary_stats(pd.DataFrame(m.resample_data(m.fetch_index_data(name))))
    st.write(stats_df)
    st.line_chart(
        (1 + pd.DataFrame(m.resample_data(m.fetch_index_data(name)))).cumprod(),
        y="Return",
    )


match select_index:
    case "S&P 500":
        index_name = "^GSPC"
        st.write("S&P 500 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)

    case "Nasdaq Composite":
        index_name = "^IXIC"
        st.write("Nasdaq Composite historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)

    case "Dow Jones Industrial Average":
        index_name = "^DJI"
        st.write("Dow Jones Industrial Average historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)

    case "Russell 2000":
        index_name = "^RUT"
        st.write("Russell 2000 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)

    case "FTSE 100":
        index_name = "^FTSE"
        st.write("FTSE 100 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)

    case "DAX PERFORMANCE-INDEX":
        index_name = "^GDAXI"
        st.write("DAX PERFORMANCE-INDEX historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)

    case "CAC 40":
        index_name = "^FCHI"
        st.write("CAC 40 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)

    case "Nikkei 225":
        index_name = "^N225"
        st.write("Nikkei 225 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)

    case "HANG SENG INDEX":
        index_name = "^HSI"
        st.write("HANG SENG INDEX historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)


st.write(index_name)
