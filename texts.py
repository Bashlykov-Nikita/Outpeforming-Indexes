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
    st.write(
        """
        - An :grey-background[index] from the companies of which portfolios will be made. 
        - In what way :orange-background[covariance matrix] will be calculated.
        - In what way :blue-background[expected return] will be calculated.
    """
    )
    st.write("##### Index:")
    st.write(
        f""" 
            1. :grey-background[🇺🇸 S&P500 ] - is a stock market index that tracks the performance of 500 of the largest companies listed on U.S. exchanges. It is widely regarded as a key barometer of the U.S. stock market's health. :green[Market-Capitalization-Weighted].\n
            2. :grey-background[🇺🇸 Nasdaq100] - is a stock market index that includes 100 of the largest non-financial companies listed on the Nasdaq Stock Market. It's heavily weighted towards technology companies, making it a popular benchmark for the tech industry. :green[Market-Capitalization-Weighted].\n
            3. :grey-background[🇺🇸 Dow Jones Industrial Average] -  is a stock market index that measures the performance of 30 large publicly-owned companies based primarily in the United States. :blue[Price-Weighted] Index.\n
            4. :grey-background[🇬🇧 FTSE 100] -  is a share index of the 100 companies listed on the London Stock Exchange with the highest market capitalization. :green[Market-Capitalization-Weighted].\n
            5. :grey-background[🇩🇪 DAX] -  is a stock market index consisting of the 40 largest German companies listed on the Frankfurt Stock Exchange. :green[Market-Capitalization-Weighted].\n
            6. :grey-background[🇭🇰 Nikkei 225] -  is a stock market index that tracks the performance of 225 of the largest companies listed on the Tokyo Stock Exchange. :blue[Price-Weighted] Index.\n
            7. :grey-background[🇯🇵 Hang Seng Index (HSI)] - is a stock market index that tracks the performance of the 80 largest companies listed on the Hong Kong Stock Exchange. :green[Market-Capitalization-Weighted]."""
    )
    attention_text(
        "Indices often include companies sharing similar characteristics, like large-cap or growth stocks. Relying solely on one index can lead to a concentrated portfolio, exposing it to specific factor risks"
    )
    st.write("##### Covariance:")
    st.write(
        f"""
            {add_spaces(6)} :orange-background[Sample] - Uses only past data. This is an extreme method that has :red[no model risk but high sample risk]. The complexity is O(n^2), which makes it computationally expensive and time-consuming to produce results. Consequently, this method can be costly.
            \n{add_spaces(6)} :orange-background[Constant Correlation Model] - A simpler method that assumes all stocks move together equally. This is an extreme method that has :red[no sample risk but high model risk]. The complexity is constant, making these calculations inexpensive to produce. This method might seem contradictory to the entire Markowitz optimization idea, as the proper usage of the covariance matrix is the way to minimize risk. However, in scenarios where the data is noisy, this method can be effective.
            \n{add_spaces(6)} :orange-background[Shrinkage Model] - This method allows us to find an optimal trade-off between sample risk and model risk. Performing statistical shrinkage is formally equivalent to introducing minimum/maximum weight constraints. In this particular project, it mixes Sample and CCM methods in a :red[50/50 proportion], but this can be adjusted to any desired ratio."""
    )
    note_text(
        "In this project, Shrinkage is balanced at 50/50, however, this is not necessarily the best approach. It is recommended to test various proportions between sample and model risk to understand which ratio is most suitable for specific portfolios"
    )
    st.write("##### Expected Return:")
    st.write(
        f"""
            {add_spaces(6)} :blue-background[Average] - is a simple average of past returns.
            \n{add_spaces(6)} :blue-background[Exponentially Weighted Average] - is a method that calculates the average of historical returns by assigning exponentially decreasing weights over time. This means that more recent data points are given more weight than older ones.
        """
    )
    attention_text(
        "You can notice that in almost all portfolios, Exponentially Weighted Average performs worse than Simple Average. This is due to the small backtest range, which means that older but still relevant data has significantly less weight than it should when creating a portfolio. To accurately assess EWA, it is necessary to increase the estimation window in backtesting"
    )
    st.divider()
    st.subheader(" About Metrics")
    st.write(
        f"{add_spaces(3)}When selecting a particular portfolio, metrics derived from historical backtesting are presented. These metrics illustrate the portfolio's past performance, along with providing insights into the likely distribution of future returns."
    )
    st.write(
        """
        1) :blue-background[Average Annual Return (AAR)]: This measures the average :grey[yearly return] of an investment over a specified period. It's calculated by taking the arithmetic mean of a series of annual returns
        2) :blue-background[Annual Volatility]: This measures the standard deviation of an investment's annual returns. It indicates how :grey[much the returns fluctuate] from the average return, providing insight into the investment's risk level.
        3) :blue-background[Skewness]: This measures the :grey[asymmetry] of the return distribution around its mean. :green[Positive skewness] indicates that the distribution has a :green[longer right tail], while :red[negative skewness] indicates a :red[longer left tail].
        4) :blue-background[Kurtosis]: This measures the :grey["tailedness"] of the return distribution. High kurtosis indicates a distribution with fat tails and a sharp peak, :red[suggesting a higher probability of extreme returns].
        5) :blue-background[Value at Risk (VaR) (5%)]: This measures the :grey[maximum potential loss] of an investment over a given time period  with a :grey[95% confidence]. It's a risk management tool used to assess the potential for extreme losses.
        6) :blue-background[Conditional Value at Risk (CVaR) (5%)]: Also known as Expected Shortfall, this measures the :grey[average loss beyond the VaR] threshold, providing a more comprehensive view of tail risk.
        7) :blue-background[Sharpe Ratio]: This measures the risk-adjusted return of an investment. It's calculated by subtracting the risk-free rate from the investment's return and dividing by its standard deviation. A higher Sharpe ratio indicates better :grey[risk-adjusted performance].
        8) :blue-background[Maximum Drawdown]: This measures the :grey[largest peak-to-trough decline] in the value of an investment over a specified period. It's an indicator of the potential loss an investor might face."""
    )
    note_text(
        "The Sharpe ratio, while useful, offers a limited view of portfolio risk by focusing solely on volatility. To assess the potential for extreme losses, investors should consider VaR, CVaR, and MDD. The effectiveness of these measures is enhanced by understanding the skewness and kurtosis of the return distribution, which can reveal valuable insights about the likelihood of tail events"
    )
    st.divider()
    st.subheader("About Backtesting")
    st.write(
        f"{add_spaces(3)}Rolling window backtesting is a valuable technique for assessing the performance and robustness of asset portfolio strategies over time. It involves creating a fixed-size window of historical data, applying the strategy to that window, and then moving the window forward by a certain interval. This process is repeated until the entire dataset has been covered."
    )
    note_text(
        "Our backtest begins in 2019 with a yearly estimation window and monthly steps. These settings can be tweaked for better accuracy. Daily data is preferred over monthly, and the backtest frequency should align with your planned rebalancing"
    )
    st.divider()
    st.subheader("How results can be improved?")
    st.write("##### Constant Proportion Portfolio Insurance (CPPI)")
    st.write(
        f"{add_spaces(3)}Constant Proportion Portfolio Insurance (CPPI) is a dynamic investment strategy that aims to provide a floor or minimum value to a portfolio while still allowing for participation in upside market movements. It's essentially a risk management technique that seeks to balance potential gains with downside protection."
    )
    st.write(
        f"{add_spaces(3)}Adding a CPPI strategy can improve portfolio performance in several ways:"
    )
    st.write("Downside Protection:")
    st.write(
        """
            - Preserves Capital: CPPI helps protect the downside by setting a floor for the portfolio's value. This means that even in a market downturn, the portfolio's value is unlikely to fall below a certain level.   
            - Reduced Volatility: By limiting downside risk, CPPI can help reduce the overall volatility of the portfolio, leading to a smoother performance trajectory.
            """
    )
    st.write("Upside Participation:")
    st.write(
        """
            - Captures Market Gains: CPPI allows investors to participate in market uptrends by investing a portion of the portfolio in a risky asset. As the market rises, the allocation to the risky asset increases, potentially leading to significant gains.
            - Dynamic Allocation: The strategy dynamically adjusts the allocation between the risky and risk-free assets based on the portfolio's value relative to the floor. This allows for greater participation in market upswings while maintaining downside protection.
            """
    )
    st.write("Improved Risk-Adjusted Returns:")
    st.write(
        """
            - Enhanced Sharpe Ratio: By limiting downside risk and maintaining upside potential, CPPI can potentially improve the Sharpe ratio of the portfolio. This means the portfolio generates higher returns for a given level of risk.
            - Better Risk-Reward Profile: CPPI can help create a more favorable risk-reward profile by providing a balance between risk and return.
            """
    )
    st.write("##### Liability-Driven Investment (LDI)")
    st.write(
        f"{add_spaces(3)} Liability-Driven Investment (LDI) is an investment strategy that focuses on matching the timing and amount of future cash flows from investments with future liabilities. It's particularly common in pension funds and insurance companies, where they have long-term obligations to pay out benefits."
    )
    st.write(f"{add_spaces(3)}Key Benefits of LDI:")
    st.write(
        """
            - Reduced Risk: By matching assets to liabilities, LDI can help reduce the risk of funding shortfalls.
            - Improved Financial Stability: LDI can contribute to the long-term financial stability of institutions by ensuring that they have sufficient assets to meet their future obligations.
            - Enhanced Investment Performance: By focusing on matching liabilities, LDI can help improve the overall investment performance of the portfolio.
            """
    )
    st.write("##### Factor Analysis")
    st.write(
        f"{add_spaces(3)}Factor analysis is a statistical technique that can be applied to financial data to identify underlying factors that drive asset returns. By understanding these factors, investors and analysts can make more informed decisions and develop effective investment strategies."
    )
    st.write(
        f"{add_spaces(3)}Factor analysis can significantly enhance portfolio performance by providing a structured approach to understanding and managing risk and return. Here's how:"
    )
    st.write(
        """
            1. Identifying Key Drivers of Returns:
            - Uncovering Hidden Patterns: Factor analysis helps uncover the underlying factors that drive asset returns, such as value, growth, momentum, and size.
            - Informed Decision-Making: By understanding these factors, investors can make more informed decisions about asset allocation and portfolio construction.
            2. Enhanced Risk Management:
            - Diversification: Factor analysis helps identify diversifiable and non-diversifiable risks. By diversifying across different factors, investors can reduce overall portfolio risk.
            - Tail Risk Management: By understanding the factors that contribute to extreme events, investors can implement strategies to mitigate tail risk.
            3. Improved Portfolio Construction:
            - Factor-Based Portfolios: Constructing portfolios based on specific factors can lead to more targeted exposure to desired risk and return characteristics.
            - Factor Tilting: Investors can tilt their portfolios towards factors that are expected to outperform, such as value or momentum.
            - Factor Timing: By analyzing the cyclical nature of factors, investors can time their exposure to different factors to optimize returns.
            4. Performance Attribution and Evaluation:
            - Understanding Performance: Factor analysis helps break down portfolio performance into its component factors, allowing investors to understand the sources of returns and identify areas for improvement.   
            - Benchmarking: Comparing factor exposures to benchmarks can help assess relative performance and identify areas of outperformance or underperformance.
            5. Risk Budgeting:
            - Allocating Risk: By understanding the factor risks in a portfolio, investors can allocate risk more effectively across different factors.   
            - Controlling Risk: Factor analysis can help identify and manage unintended factor exposures that could increase portfolio risk. """
    )
    st.write("##### Sources")
