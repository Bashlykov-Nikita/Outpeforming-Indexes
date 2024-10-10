import streamlit as st
import Outperforming as Out

st.set_page_config(
    page_title="Outperforming Indexes",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.write("### :bar_chart: Used data")

st.write(st.session_state["select_cov"])
st.write(st.session_state["select_er"])
