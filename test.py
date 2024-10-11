import numpy as np
import pandas as pd
import yfinance as yf
import calc as c
import data as d

test = c.summary_stats(pd.DataFrame(d.get_df(d.BACKTEST["DowJones"])["EW"]))

test[["Annualized Return", "Annualized Vol", "Sharpe Ratio", "Max Drawdown"]]

match select_index:
    case "None":
        # TODO: Starting page
        st.write("Choose index you want to ouperform")

    case "SP500":
        index_name = "^GSPC"
        components_returns_url = 0

        st.write("S&P 500 historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "Nasdaq100":
        index_name = "^IXIC"
        components_returns_url = 1

        st.write("Nasdaq Composite historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "DowJones":
        index_name = "^DJI"
        components_returns_url = 2

        st.write("Dow Jones Industrial Average historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "FTSE100":
        index_name = "^FTSE"
        components_returns_url = 3

        st.write("FTSE 100 historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "DAX":
        index_name = "^GDAXI"
        components_returns_url = 4
        st.write("DAX PERFORMANCE-INDEX historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "CAC40":
        index_name = "^FCHI"
        components_returns_url = None
        st.write("CAC 40 historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "Nikkei225":
        index_name = "^N225"
        components_returns_url = None
        st.write("Nikkei 225 historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "HSI":
        index_name = "^HSI"
        components_returns_url = 5
        st.write("HANG SENG INDEX historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)
