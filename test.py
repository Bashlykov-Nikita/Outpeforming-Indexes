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
comp = pd.DataFrame(get_components(components_url))
comp = pd.DataFrame(columns=comp["Symbol"])
comp = comp.apply(
    lambda x: 1,
    axis=1,
)


# get_components(components_url)[]
def func(col_name):
    return yf.Ticker(col_name).history(period="max")["Open"]


comp = comp.apply(lambda x: func(x), axis=1)


# Create a list of company tickers
tickers = get_components(components_url)
first_ticker_data = yf.download("AAPL", period="max")
# Create an empty DataFrame with a single row
df = pd.DataFrame(index=first_ticker_data.index, columns=tickers)

# Fetch historical data for each ticker and populate the DataFrame
for ticker in tickers:
    try:
        data = yf.download(ticker, period="max")
        if data["Open"] == 0:
            df[ticker] = None
        else:
            data["Return"] = (data["Close"] - data["Open"]) / data["Open"]
            df[ticker] = data["Open"]
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        df[ticker] = None  # Or handle the error differently, e.g., fill with 0

df
get_components(components_url)[0]


def companies_returns_df(companies):
    tickers = companies
    first_ticker_data = yf.download(companies[0], period="max")
    # Create an empty DataFrame with a single row
    companies_df = pd.DataFrame(index=first_ticker_data.index, columns=tickers)

    # Fetch historical data for each ticker and populate the DataFrame
    for ticker in tickers:
        try:
            data = yf.download(ticker, period="max")
            if data.empty:
                companies_df[ticker] = 0
            else:
                data["Return"] = (data["Close"] - data["Open"]) / data["Open"]
                companies_df[ticker] = data["Return"]
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            companies_df[ticker] = (
                None  # Or handle the error differently, e.g., fill with 0
            )
    return companies_df


companies_returns_df(get_components(components_url))

test_data = yf.download(get_components(components_url)[3], start="1980-01-01")
test_data.empty
