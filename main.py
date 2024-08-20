import numpy as np
import pandas as pd
import yfinance as yf

import calc as c


# TODO: Unify
def data_for_plots(index_name):
    index_data = yf.Ticker(index_name)
    index_data = index_data.history(period="max")
    mask = index_data["Open"] == 0
    index_data = index_data[~mask]
    index_data["Return"] = (index_data["Close"] - index_data["Open"]) / index_data[
        "Open"
    ]
    return index_data["Return"]


def fetch_index_data(index_name):
    index_data = yf.Ticker(index_name)

    index_data = index_data.history(period="max")
    # del index_data["Dividends"]
    # del index_data["Stock Splits"]
    index_data.index = index_data.index.to_period("D")
    mask = index_data["Open"] == 0
    index_data = index_data[~mask]
    index_data["Return"] = (index_data["Close"] - index_data["Open"]) / index_data[
        "Open"
    ]
    index_data = index_data.dropna()
    return index_data


def resample_data(index_data):
    index_data = index_data.to_timestamp()
    index_data_m = index_data.resample("M").apply(c.compound).to_period("M")
    return index_data_m


def get_components(url):
    if url:
        return pd.read_csv(url)["Symbol"]
    else:
        return "Components data is not available yet :("


# Calculating all the history returns for all companies


def companies_returns_df(companies):
    companies_returns = pd.DataFrame()
    i = 0
    # for company_name in companies:
    #     company = yf.Ticker(company_name)
    #     company = company.history(period="max")
    #     company = company["1990":].copy()
    #     company[f"{company_name}"] = (company["Close"] - company["Open"]) / company[
    #         "Open"
    #     ]
    #     company = company.dropna()
    #     companies_returns.insert(
    #         loc=i, column=f"{company_name}", value=company[f"{company_name}"]
    #     )
    # i = i + 1
    while i < companies.shape[0]:
        company = yf.Ticker(companies[i]).history(period="max")

    return companies_returns


def test(companies):
    # company = yf.Ticker(companies[0])
    # company = company.history(period="max")
    # company.index = company.index.to_period("D")
    # company = resample_data(company)
    i = 0
    # for company_name in companies:
    while i < companies.shape[0]:
        try:
            c_h = fetch_index_data(companies[i])
            i = i + 1
        except:
            return i
    return c_h


def test1(companies):
    i = 0
    test_df = pd.DataFrame()
    # if (yf.Ticker(companies[7]).history(period="max")).empty:
    #     return False
    # else:
    #     return yf.Ticker(companies[7]).history(period="max")
    # while i < companies.shape[0]:
    #     company = yf.Ticker(companies[i]).history(period="max")
    #     if company.empty:
    #         test_df.insert(loc=i, column=f"{companies[i]}", value=0)
    #         i = i + 1
    #     else:
    #         test_df.insert(loc=i, column=f"{companies[i]}", value=1)
    #         i = i + 1
    for company in companies:
        company = yf.Ticker(companies[i]).history(period="max")
        if company.empty:
            test_df.insert(loc=i, column=f"{companies[i]}", value=0)
            i = i + 1
        else:
            test_df.insert(loc=i, column=f"{companies[i]}", value=1)
            i = i + 1

    return test_df
