import sys

sys.dont_write_bytecode = True
import numpy as np
import pandas as pd
import yfinance as yf
import calc as c
import data as d
import get

test = get.get_df(d.PORTFOLIOS_WEIGHTS["DAX"])["GMV_Sample"]
test1 = test.sort_values(ascending=False)
test2 = pd.DataFrame(test1)
test3 = test2.T
