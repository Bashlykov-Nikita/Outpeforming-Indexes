import streamlit as st


def index_none_text():
    return ""


def portfolio_none_text(selected_portfolio):
    portfolios_desc = """Maximum Sharpe Ratio - a portfolio that aims for the highest possible returns for a given level of risk.
Global Minimum Variance - a portfolio with the smallest possible fluctuations in value.
Equally Weighted - a portfolio where each stock has the same percentage.
Cap Weighted - a portfolio where each stock's weight is based on its market value.
Equal Risk Contribution - a portfolio where each stock contributes equally to the overall portfolio risk."""
    if selected_portfolio == "None":
        st.markdown(portfolios_desc)
