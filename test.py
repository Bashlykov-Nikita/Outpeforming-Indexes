import numpy as np
import pandas as pd
import yfinance as yf
import calc as c

index_name = "^GSPC"
components_url = "https://yfiua.github.io/index-constituents/constituents-sp500.csv"


def get_components(url):
    if url:
        return pd.read_csv(url)["Symbol"]
    else:
        return "Components data is not available yet :("


def test1(companies):
    i = 0
    companies_returns = pd.DataFrame()

    for company in companies:
        company = yf.Ticker(companies[i]).history(period="max")
        try:
            company.index = company.index.to_period("D")
            company["Return"] = (company["Close"] - company["Open"]) / company["Open"]
            company = company["Return"]
            company = company.to_timestamp()
            company = company.resample("M").apply(c.compound).to_period("M")
            companies_returns.insert(
                loc=i, column=f"{companies[i]}", value=company[f"{company}"]
            )
        except:
            companies_returns.insert(loc=i, column=f"{companies[i]}", value=None)
    return companies_returns


test_df = pd.DataFrame()
test_df = pd.DataFrame(
    [get_components(components_url)[0], get_components(components_url)[1]]
)
yf.Ticker(test_df.T[0][0]).history(period="max")

test1(test_df)
# get_components(components_url)[]
