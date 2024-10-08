import pandas as pd
import streamlit as st
import main as m
import calc as c

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
