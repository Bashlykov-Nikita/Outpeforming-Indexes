import sys

sys.dont_write_bytecode = True
import streamlit as st
import data as d
import show

#! Streamlit page
# * Data showcase streamlit page

# ? Configuring page
st.set_page_config(
    page_title="Outperforming Indexes",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.write("# :bar_chart: Used data")

# ? Fetching session state values from Outperforming page
selected_index = st.session_state["select_index"]
selected_cov = st.session_state["select_cov"]
selected_er = st.session_state["select_er"]
# st.write(st.session_state["select_cov"])
# st.write(st.session_state["select_er"])
# st.write(st.session_state["select_index"])
if selected_index != "None":
    # ? Show Index historical data:
    st.write(f"#### {selected_index} historical data:")
    show.show_index_hist_data(d.INDEXES[selected_index])

    # ? Show portfolios weights:
    st.write("#### Recommended portfolios weights:")
    st.write(
        f"With **{selected_cov}** covariance and **{selected_er}** expected return"
    )
    show.show_portfolios_weights_and_backtest(selected_index, selected_cov, selected_er)

    # ? Show Backtest:
    st.write("#### Backtest data:")
    st.caption("_Backtest of Cap Weighted portfolio is not done yet._")
    show.show_portfolios_weights_and_backtest(
        selected_index, selected_cov, selected_er, backtest=True
    )

    # ? Link to Github:
    st.write(
        "To know more on how this portfolios were created and backtested click [here](https://github.com/Bashlykov-Nikita/Creating-Portfolio/tree/main)."
    )
else:
    # ? If index was not chosen:
    st.write("Choose index")
