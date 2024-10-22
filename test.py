import sys

sys.dont_write_bytecode = True
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.figure_factory as ff
import calc as c
import data as d
import get
import utils

test = get.get_df(d.BACKTEST["SP500"])["GMV_Sample"]
test1 = pd.DataFrame({"Date": test.index, "Returns": test.values})
bt_df = pd.DataFrame(
    {"Timeline": test1["Date"], "Return": (1 + test1["Returns"]).cumprod()}
)


sp500 = get.get_index_data(d.INDEXES["SP500"], True)
sp500_df = pd.DataFrame(sp500)
sp500_m = utils.resample_data(sp500_df)


test5 = utils.resample_data(get.get_index_data(d.INDEXES["SP500"]))["2020-01":]
test6 = test5["Return"]
index_returns_df = pd.DataFrame(
    {"Date": test6.index, "SP500": (1 + test6.values).cumprod()}
)
bt_df["SP500"] = index_returns_df["SP500"]

fig = px.line(bt_df, x="Timeline", y=["Return", "SP500"], title="Growth Plot:")
fig.show()

fig1 = px.line(index_returns_df, x="Date", y="SP500", title="Growth Plot:")
fig1.show()
