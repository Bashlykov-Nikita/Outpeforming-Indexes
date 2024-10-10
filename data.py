import pandas as pd

# * File with url constatns:

INDEXES = [
    "None",
    "SP500",
    "Nasdaq100",
    "DowJones",
    "FTSE100",
    "DAX",
    "CAC40",
    "Nikkei225",
    "HSI",
]

COV = ["Sample", "Constant Correlation", "Shinkage"]
ER = ["Average", "Exponentially Weighted Average"]

BACKTEST = {
    name: f"https://github.com/Bashlykov-Nikita/Creating-Portfolio/blob/main/backtest_portfolios_data/{name}_backtest_portfolios.csv?raw=true"
    for name in INDEXES
}
PORTFOLIOS_WEIGHTS = {
    name: f"https://github.com/Bashlykov-Nikita/Creating-Portfolio/blob/main/portfolios_data/{name}_portfolios.csv?raw=true"
    for name in INDEXES
}


def get_df(url: str) -> pd.DataFrame:
    """Reads a CSV file from the specified URL and returns a DataFrame.

    Args:
        url (str): The URL of the CSV file to read.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(url, index_col=0)
