import pandas as pd

# * File with url constatns:

INDEXES = {
    "SP500": "^GSPC",
    "Nasdaq100": "^IXIC",
    "DowJones": "^DJI",
    "FTSE100": "^FTSE",
    "DAX": "^GDAXI",
    "CAC40": "^FCHI",
    "Nikkei225": "^N225",
    "HSI": "^HSI",
}

COV = {"Sample": "Sample", "Constant Correlation": "CCM", "Shinkage": "Shinkage"}
ER = {"Average": "Average", "Exponentially Weighted Average": "EWA"}

BACKTEST = {
    name: f"https://github.com/Bashlykov-Nikita/Creating-Portfolio/blob/main/backtest_portfolios_data/{name}_backtest_portfolios.csv?raw=true"
    for name in INDEXES.keys()
}
PORTFOLIOS_WEIGHTS = {
    name: f"https://github.com/Bashlykov-Nikita/Creating-Portfolio/blob/main/portfolios_data/{name}_portfolios.csv?raw=true"
    for name in INDEXES.keys()
}


def get_df(url: str) -> pd.DataFrame:
    """Reads a CSV file from the specified URL and returns a DataFrame.

    Args:
        url (str): The URL of the CSV file to read.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(url, index_col=0)
