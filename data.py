import pandas as pd

# * File with url constatns:

INDEXES = {
    "SP500": "^GSPC",
    "Nasdaq100": "^IXIC",
    "DowJones": "^DJI",
    "FTSE100": "^FTSE",
    "DAX": "^GDAXI",
    # "CAC40": "^FCHI",
    "Nikkei225": "^N225",
    "HSI": "^HSI",
}

COV = {"Sample": "Sample", "Constant Correlation": "CCM", "Shrinkage": "Shrinkage"}
ER = {"Average": "Average", "Exponentially Weighted Average": "EWA"}
PORTFOLIOS_NAMES = {
    "Maximum Sharpe Ratio": "MSR",
    "Global Minimum Variance": "GMV",
    "Equally Weighted": "EW",
    # "Cap Weighted": "CW",
    "Equal Risk Contribution": "ERC",
}

BACKTEST = {
    name: f"https://github.com/Bashlykov-Nikita/Creating-Portfolio/blob/main/backtest_portfolios_data/{name}_backtest_portfolios.csv?raw=true"
    for name in INDEXES.keys()
}
PORTFOLIOS_WEIGHTS = {
    name: f"https://github.com/Bashlykov-Nikita/Creating-Portfolio/blob/main/portfolios_data/{name}_portfolios.csv?raw=true"
    for name in INDEXES.keys()
}

HELP = {
    "Return": "Average return over a year.",
    "Volatility": "How much an investment's value fluctuates yearly.",
    "Sharpe Ratio": "Risk-adjusted return.",
    "Max Drawdown": "Largest potential loss.",
    "Skewness": "Measures asymmetry of distribution.",
    "Kurtosis": 'Measures "tailedness" of distribution.',
    "VaR (5%)": "(Cornish-Fisher) Maximum potential loss at a given confidence level.",
    "CVaR (5%)": "(Historic) Expected loss beyond VaR.",
}
