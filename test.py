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

risk_free_rate = 0.02
market_return = 0.08
market_std_dev = 0.15

# Calculate the CML points
cml_points = pd.DataFrame(
    {
        "Standard Deviation": [0, market_std_dev],
        "Expected Return": [risk_free_rate, market_return],
    }
)

# Add the CML to the plot
fig.add_trace(
    go.Scatter(
        x=cml_points["Standard Deviation"],
        y=cml_points["Expected Return"],
        mode="lines",
        name="CML",
    )
)

fig.show()
