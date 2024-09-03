import streamlit as st
import numpy as np
import pandas as pd
import main as m
import calc as c
import time
import matplotlib.pyplot as plt


st.title("Outperforming Indexes")
st.markdown(" Data from Yahoo Finance ")

with st.sidebar:

    st.title("Options")

    select_index = st.selectbox(
        "Choose Index",
        (
            "None",
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


# @st.cache_data
def show_index_historical_data(name):
    st.write(m.fetch_index_data(name))


# @st.cache_data
def show_stats(name):
    m_ind_data = pd.DataFrame(m.resample_data(m.fetch_index_data(name))["Return"])
    stats_df = c.summary_stats(m_ind_data)
    st.write(stats_df)


# @st.cache_data
def growth_plot(name):
    st.line_chart(data=(1 + m.fetch_index_data(name, True)).cumprod(), y="Return")


match select_index:
    case "None":
        # TODO: Starting page
        st.write("Choose index you want to ouperform")

    case "S&P 500":
        index_name = "^GSPC"
        components_returns_url = 0

        st.write("S&P 500 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "Nasdaq Composite":
        index_name = "^IXIC"
        components_returns_url = 1

        st.write("Nasdaq Composite historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "Dow Jones Industrial Average":
        index_name = "^DJI"
        components_returns_url = 2

        st.write("Dow Jones Industrial Average historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "Russell 2000":
        index_name = "^RUT"
        components_returns_url = None
        st.write("Russell 2000 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "FTSE 100":
        index_name = "^FTSE"
        components_returns_url = 3

        st.write("FTSE 100 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "DAX PERFORMANCE-INDEX":
        index_name = "^GDAXI"
        components_returns_url = 4
        st.write("DAX PERFORMANCE-INDEX historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "CAC 40":
        index_name = "^FCHI"
        components_returns_url = None
        st.write("CAC 40 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "Nikkei 225":
        index_name = "^N225"
        components_returns_url = None
        st.write("Nikkei 225 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "HANG SENG INDEX":
        index_name = "^HSI"
        components_returns_url = 5
        st.write("HANG SENG INDEX historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)
