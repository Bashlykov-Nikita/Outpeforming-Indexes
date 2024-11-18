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


def add_spaces(number_of_spaces):
    return " &nbsp;" * number_of_spaces


def portfolio_none_text(selected_portfolio):
    if selected_portfolio == "None":
        st.subheader("About Portfolios:")
        st.write(
            """##### - 📈Maximum Sharpe Ratio - a portfolio that aims for the highest possible returns for a given level of risk."""
        )
        st.markdown(
            """An MSR portfolio is an investment portfolio designed to maximize the Sharpe ratio. The Sharpe ratio is a measure of :blue-background[risk-adjusted return], calculated as the excess return of an investment compared to a risk-free rate, :blue-background[divided by its standard deviation].
            \nIn essence, an MSR portfolio aims to achieve :blue-background[the highest possible return for a given level of risk]. It's a popular strategy used by investors and portfolio managers to optimize their investments."""
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
            """A Global Minimum Variance (GMV) portfolio is an investment portfolio designed to :blue-background[minimize risk], specifically the portfolio's variance or standard deviation. 
                It's constructed by identifying the specific weights for each asset in the portfolio that result in the lowest possible overall risk."""
        )
        st.markdown(
            """GMV is not consistently better than the [1/N rule](https://academic.oup.com/rfs/article-abstract/22/5/1915/1592901?redirectedFrom=fulltext) in terms of Sharpe Ratio. But GMV :blue-background[can be improved]:
            \n- Solution 1: GMV with a minimum :blue-background[Effective Number of Constituents (ENC)] constraint.
            \n- Solution 2: Select all assets with the same volatility (This portfolio is sometimes known as the "Max Decorrelation Portfolio").
            \n In both cases, it forces the optimizer to make :blue-background[smart use of the correlation structure], as opposed to merely overweighting low-volatility components."""
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
            """An Equal-Weighted (EW) portfolio is a type of investment portfolio where :blue-background[each asset] in the portfolio is assigned an :blue-background[equal weight]. This means that the same amount of money is invested in each asset, regardless of its market capitalization."""
        )
        attention_text(
            "An EW portfolio represents an extreme case of a fully balanced portfolio, prioritizing equal dollar contributions (EW = Max ENC). This type of portfolio is inexpensive to construct as it doesn't necessitate any return or risk estimation. However, the diversification benefits of such an approach may not always yield optimal results"
        )
        st.write(
            "##### - 🧩Equal Risk Contribution - a portfolio where each stock contributes equally to the overall portfolio risk."
        )
        st.markdown(
            """An ERC portfolio, also known as an Equal Risk Contribution portfolio, is a type of investment portfolio that aims to :blue-background[distribute risk equally] among its constituent assets. This means that each asset in the portfolio contributes the same amount of risk to the overall portfolio. """
        )
        note_text(
            "While portfolios balanced by dollar contributions may appear well-diversified, they can still be highly concentrated in terms of risk. Understanding the risk contribution of each asset is crucial for effective portfolio management"
        )


def index_none_text():
    st.subheader("Overview")
    st.write("##### The main idea of this project:")
    st.write(
        "Develop a robust investment portfolio optimization framework that generates diverse portfolio strategies based on popular financial indexes."
    )
    st.write("##### What this programme does:")
    st.write(
        """- Web-scraping companies names
        \n- Getting companies historical returns
        \n- Creating different types of portfolios
        \n- Backtesting
        \n- Risk analysis and performance evaluation
        \n- Visualization and reporting"""
    )
    st.write("##### Why outperform the indexes?")
    st.write(
        "The index serves as a benchmark to measure the portfolio's alpha or excess return. A positive difference between the portfolio's performance and the index's performance indicates value creation. By aiming to outperform the index, we strive to generate superior returns."
    )
    st.divider()
    st.subheader("About Options")
    st.write(
        "This project automatically rebalances 168 investment portfolios monthly. To view a specific portfolio, choose the relevant options:"
    )
    st.write("##### 1. Index:")
    st.write(
        f""" 
                {add_spaces(6)} 🇺🇸 :grey-background[S&P500] - is a stock market index that tracks the performance of 500 of the largest companies listed on U.S. exchanges. It is widely regarded as a key barometer of the U.S. stock market's health. :green[Market-Capitalization-Weighted].
                \n{add_spaces(6)} 🇺🇸 :grey-background[Nasdaq100] - is a stock market index that includes 100 of the largest non-financial companies listed on the Nasdaq Stock Market. It's heavily weighted towards technology companies, making it a popular benchmark for the tech industry. :green[Market-Capitalization-Weighted].
                \n{add_spaces(6)} 🇺🇸 :grey-background[Dow Jones Industrial Average] -  is a stock market index that measures the performance of 30 large publicly-owned companies based primarily in the United States. :blue[Price-Weighted] Index.
                \n{add_spaces(6)} 🇬🇧 :grey-background[FTSE 100] -  is a share index of the 100 companies listed on the London Stock Exchange with the highest market capitalization. :green[Market-Capitalization-Weighted].
                \n{add_spaces(6)} 🇩🇪 :grey-background[DAX] -  is a stock market index consisting of the 40 largest German companies listed on the Frankfurt Stock Exchange. :green[Market-Capitalization-Weighted].
                \n{add_spaces(6)} 🇭🇰 :grey-background[Nikkei 225] -  is a stock market index that tracks the performance of 225 of the largest companies listed on the Tokyo Stock Exchange. :blue[Price-Weighted] Index.
                \n{add_spaces(6)} 🇯🇵 :grey-background[Hang Seng Index (HSI)] - is a stock market index that tracks the performance of the 80 largest companies listed on the Hong Kong Stock Exchange. :green[Market-Capitalization-Weighted]."""
    )
    attention_text("Tilt")
    st.write("##### 2. Covariance:")
    st.write(
        f"""{add_spaces(6)} :orange-background[Sample] - Uses only past data. This is an extreme method that has :red[no model risk but high sample risk]. The complexity is O(n^2), which makes it computationally expensive and time-consuming to produce results. Consequently, this method can be costly.
                \n{add_spaces(6)} :orange-background[Constant Correlation Model] - A simpler method that assumes all stocks move together equally. This is an extreme method that has :red[no sample risk but high model risk]. The complexity is constant, making these calculations inexpensive to produce. This method might seem contradictory to the entire Markowitz optimization idea, as the proper usage of the covariance matrix is the way to minimize risk. However, in scenarios where the data is noisy, this method can be effective.
                \n{add_spaces(6)} :orange-background[Shrinkage Model] - This method allows us to find an optimal trade-off between sample risk and model risk. Performing statistical shrinkage is formally equivalent to introducing minimum/maximum weight constraints. In this particular project, it mixes Sample and CCM methods in a :red[50/50 proportion], but this can be adjusted to any desired ratio."""
    )
    st.write("##### About Metrics")
    st.write("##### About Backtesting")
    st.write("##### How results can be improved?")
    st.write("##### Sources")
