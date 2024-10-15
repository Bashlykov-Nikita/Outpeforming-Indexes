import sys

sys.dont_write_bytecode = True
import streamlit as st
import data as d
import show
import main as m

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


def add_none_to_list(l: list):
    return ["None"] + l


with st.sidebar:
    st.title("Options")

    st.session_state.select_index = st.selectbox(
        label="Choose Index",
        options=add_none_to_list(list(d.INDEXES.keys())),
        index=(
            add_none_to_list(list(d.INDEXES.keys())).index(
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
    label="Select Portfolio", options=add_none_to_list(list(d.PORTFOLIOS_NAMES.keys()))
)

st.write(m.select_portfolio_name(selected_portfolio, selected_cov, selected_er))
chosen_portfolio = m.select_portfolio_name(
    selected_portfolio, selected_cov, selected_er
)
weights = m.get_certain_portfolio(selected_index, chosen_portfolio)[0]
# show.show_df(d.get_df(d.PORTFOLIOS_WEIGHTS[selected_index])[chosen_portfolio])
st.write(weights)

total1, total2, total3, total4, total5 = st.columns(5, gap="small")
with total1:
    st.info("Sum Investment", icon="💰")
    st.metric(label="Sum TZS", value=f"{1:,.0f}")

with total2:
    st.info("Most Investment", icon="💰")
    st.metric(label="Mode TZS", value=f"{2:,.0f}")

with total3:
    st.info("Average", icon="💰")
    st.metric(label="Average TZS", value=f"{3:,.0f}")

with total4:
    st.info("Central Earnings", icon="💰")
    st.metric(label="Median TZS", value=f"{4:,.0f}")

with total5:
    st.info("Ratings", icon="💰")
    st.metric(label="Rating", value=5, help=f""" Total Rating: {5} """)
