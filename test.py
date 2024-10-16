import numpy as np
import pandas as pd
import yfinance as yf
import calc as c
import data as d

test = d.get_df(d.BACKTEST["SP500"])
cov_short = d.COV["Sample"]
er_short = d.ER["Average"]
p_arr = [
    f"MSR_{cov_short}_{er_short}",
    f"GMV_{cov_short}",
    "EW",
    "CW",
    f"ERC_{cov_short}",
]
p_arr2 = p_arr[:3] + p_arr[4:]
test1 = d.get_df(d.BACKTEST["SP500"])[p_arr2]
test1.head()


def find_matching_column(df, prefix):
    """Finds a column in the DataFrame that starts with the given prefix.

    Args:
        df: The DataFrame to search.
        prefix: The prefix to match.

    Returns:
        The column name if found, or None if not found.
    """

    for col in df.columns:
        if col.startswith(prefix):
            return col
    return None


# Example usage:
data = {"col1": ["a", "b", "c"], "col2": [1, 2, 3], "col3": ["x", "y", "z"]}
df = pd.DataFrame(data)
prefix = "col"
result = find_matching_column(df, prefix)
print(result)  # Output: "col1"
