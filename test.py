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
p_arr2 = p_arr.remove("CW")
test1 = d.get_df(d.BACKTEST["SP500"])[p_arr2]
