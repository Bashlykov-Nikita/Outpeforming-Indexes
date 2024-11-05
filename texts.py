import streamlit as st


def index_none_text():
    return ""


def portfolio_none_text(selected_portfolio):
    if selected_portfolio == "None":
        st.subheader("About Portfolios:")
        st.write(
            "#### - 📈Maximum Sharpe Ratio - a portfolio that aims for the highest possible returns for a given level of risk."
        )
        st.markdown(
            """
        <div class="note-block">
            <strong>Note:</strong> This is an important note for the user.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <style>
            .note-block {
                padding: 1rem;
                border-radius: 0.5rem;
                background-color: #062633;
                border-left: 4px solid rgb(0 192 242 / 1);
                margin-bottom: 1rem;
            }
        </style>
        """,
            unsafe_allow_html=True,
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
