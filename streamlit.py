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


@st.cache_data
def show_index_historical_data(name):
    st.write(m.fetch_index_data(name))


@st.cache_data
def show_stats(name):
    m_ind_data = pd.DataFrame(m.resample_data(m.fetch_index_data(name))["Return"])
    stats_df = c.summary_stats(m_ind_data)
    st.write(stats_df)


@st.cache_data
def growth_plot(name):
    st.line_chart(data=(1 + m.data_for_plots(name)).cumprod(), y="Return")


match select_index:
    case "S&P 500":
        index_name = "^GSPC"
        components_url = (
            "https://yfiua.github.io/index-constituents/constituents-sp500.csv"
        )

        st.write("S&P 500 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "Nasdaq Composite":
        index_name = "^IXIC"
        components_url = (
            "https://yfiua.github.io/index-constituents/constituents-nasdaq100.csv"
        )

        st.write("Nasdaq Composite historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "Dow Jones Industrial Average":
        index_name = "^DJI"
        components_url = (
            "https://yfiua.github.io/index-constituents/constituents-dowjones.csv"
        )

        st.write("Dow Jones Industrial Average historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "Russell 2000":
        index_name = "^RUT"
        components_url = None
        st.write("Russell 2000 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "FTSE 100":
        index_name = "^FTSE"
        components_url = (
            "https://yfiua.github.io/index-constituents/constituents-ftse100.csv"
        )

        st.write("FTSE 100 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "DAX PERFORMANCE-INDEX":
        index_name = "^GDAXI"
        components_url = (
            "https://yfiua.github.io/index-constituents/constituents-dax.csv"
        )
        st.write("DAX PERFORMANCE-INDEX historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "CAC 40":
        index_name = "^FCHI"
        components_url = None
        st.write("CAC 40 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "Nikkei 225":
        index_name = "^N225"
        components_url = None
        st.write("Nikkei 225 historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)

    case "HANG SENG INDEX":
        index_name = "^HSI"
        components_url = (
            "https://yfiua.github.io/index-constituents/constituents-hsi.csv"
        )
        st.write("HANG SENG INDEX historical data:")

        show_index_historical_data(index_name)
        show_stats(index_name)
        growth_plot(index_name)


# st.write(m.companies_returns_df(m.get_components(components_url)))
# st.write(m.test(m.get_components(components_url)))
st.write(m.test1(m.get_components(components_url)))
