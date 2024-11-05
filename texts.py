import streamlit as st


def index_none_text():
    return ""


def portfolio_none_text(selected_portfolio):
    if selected_portfolio == "None":
        st.subheader("About Portfolios:")
        st.write(
            "#### - 📈Maximum Sharpe Ratio - a portfolio that aims for the highest possible returns for a given level of risk."
        )
        st.write(
            "#### - 🛡️Global Minimum Variance - a portfolio with the smallest possible fluctuations in value."
        )
        st.write(
            "#### - ⚖️Equally Weighted - a portfolio where each stock has the same percentage."
        )
        st.write(
            "#### - 🧩Equal Risk Contribution - a portfolio where each stock contributes equally to the overall portfolio risk."
        )
