import sys

sys.dont_write_bytecode = True
import streamlit as st
import data as d
import show

if "select_index" not in st.session_state:
    st.session_state["select_index"] = "None"
if "select_cov" not in st.session_state:
    st.session_state["select_cov"] = "Sample"
if "select_er" not in st.session_state:
    st.session_state["select_er"] = "Average"

st.set_page_config(
    page_title="Outperforming Indexes",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title(":chart: Outperforming the Indexes")
st.markdown(" Data from Yahoo Finance ")

add_none_to_indexes = ["None"] + list(d.INDEXES.keys())

with st.sidebar:
    st.title("Options")

    st.session_state.select_index = st.selectbox(
        label="Choose Index",
        options=add_none_to_indexes,
        index=(add_none_to_indexes.index(st.session_state["select_index"])),
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
select_er = st.session_state.select_er
select_cov = st.session_state.select_cov
select_index = st.session_state.select_index

show.show_index_data(select_index)


match select_cov:
    case "Sample":
        cov = "Sample"
    case "Constant Correlation":
        cov = "CCM"
    case "Shinkage":
        cov = "Shinkage"

match select_er:
    case "Average":
        er = "Average"
    case "Exponentially Weighted Average":
        er = "EWA"


# st.session_state["select_cov"] = cov

# st.session_state["select_er"] = er
