import numpy as np
import pandas as pd
import yfinance as yf
import calc as c
import data as d

test = c.summary_stats(pd.DataFrame(d.get_df(d.BACKTEST["DowJones"])["EW"]))

test[["Annualized Return", "Annualized Vol", "Sharpe Ratio", "Max Drawdown"]]
