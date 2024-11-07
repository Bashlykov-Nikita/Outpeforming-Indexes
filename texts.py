import streamlit as st


def note_text(note_message: str):
    st.markdown(
        f"""
    <div class="note-block">
        <strong class="note-text">📌Note:</strong> {note_message}.
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

        }
        .note-text {
            color: rgb(0 192 242 / 1)
        }

    </style>
    """,
        unsafe_allow_html=True,
    )


def attention_text(attention_message: str):
    st.markdown(
        f"""
    <div class="attention-block">
        <strong class="attention-text">🔥Important:</strong> {attention_message}.
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <style>
        .attention-block {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #481d00;
            border-left: 4px solid rgb(255 164 33 / 1);
            margin-bottom: 1rem;
        }
        .attention-text {
            color: rgb(255 164 33 / 1)
        }

    </style>
    """,
        unsafe_allow_html=True,
    )


def index_none_text():
    return ""


def portfolio_none_text(selected_portfolio):
    if selected_portfolio == "None":
        st.subheader("About Portfolios:")
        st.write(
            """##### - 📈Maximum Sharpe Ratio - a portfolio that aims for the highest possible returns for a given level of risk."""
        )
        st.markdown(
            """An MSR portfolio is an investment portfolio designed to maximize the Sharpe ratio. The Sharpe ratio is a measure of risk-adjusted return, calculated as the excess return of an investment compared to a risk-free rate, divided by its standard deviation.
            \nIn essence, an MSR portfolio aims to achieve the highest possible return for a given level of risk. It's a popular strategy used by investors and portfolio managers to optimize their investments."""
        )
        note_text(
            "MSR portfolio contains no exposure to unrewarded risk (contains only systematic risc). That's what makes such type of portfolio so desirable"
        )
        attention_text(
            "Estimation error is a key challenge in portfolio optimization. Various methods exist for improving estimates for expected return and covariance parameters. However, some uncertainty always remains, which is particularly large for expected return"
        )
        st.write(
            "##### - 🛡️Global Minimum Variance - a portfolio with the smallest possible fluctuations in value."
        )
        st.markdown(
            """A Global Minimum Variance (GMV) portfolio is an investment portfolio designed to minimize risk, specifically the portfolio's variance or standard deviation. 
                It's constructed by identifying the specific weights for each asset in the portfolio that result in the lowest possible overall risk."""
        )
        st.markdown(
            """GMV is not consistently better than the [1/N rule](https://academic.oup.com/rfs/article-abstract/22/5/1915/1592901?redirectedFrom=fulltext) in terms of Sharpe Ratio. But GMV can be improved:
            \n- Solution 1: GMV with a minimum Effective Number of Constituents (ENC) constraint.
            \n- Solution 2: Select all assets with the same volatility (This portfolio is sometimes known as the "Max Decorrelation Portfolio").
            \n In both cases, it forces the optimizer to make smart use of the correlation structure, as opposed to merely overweighting low-volatility components."""
        )
        note_text(
            "The GMV is least sensitive to errors in parameter estimates. Since it requires no expected return estimates, it is only sensitive to errors in risk parameter estimates"
        )
        attention_text(
            'GMV implicitly assumes constant expected returns, which is not a highly reasonable prior. The "magic" of diversification may not work as expected, as low-volatility components are not penalized and may be overweighted. As a result, GMV portfolios might not be well-balanced'
        )

        st.write(
            "##### - ⚖️Equally Weighted - a portfolio where each stock has the same percentage."
        )
        st.markdown(
            """An Equal-Weighted (EW) portfolio is a type of investment portfolio where each asset in the portfolio is assigned an equal weight. This means that the same amount of money is invested in each asset, regardless of its market capitalization."""
        )
        st.write(
            "##### - 🧩Equal Risk Contribution - a portfolio where each stock contributes equally to the overall portfolio risk."
        )
