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

test = get.get_df(d.BACKTEST["SP500"])["GMV_Sample"]
test1 = pd.DataFrame({"Date": test.index, "Returns": test.values})

fig = px.histogram(test1["Returns"], histnorm="probability", marginal="box")
fig.show()

x1 = np.array(test1["Returns"])
group_label = ["Returns"]

fig = ff.create_distplot(
    [x1],
    group_label,
    bin_size=0.5,
    curve_type="normal",  # override default 'kde'
    show_hist=False,
)
fig.show()
