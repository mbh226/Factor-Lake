from MarketObject import load_data, MarketObject
from portfolio import Portfolio
from CalculateHoldings import rebalance_portfolio
import pandas as pd

def main():
    ### Load market data ###
    print("Loading market data...")
    rdata = load_data()

    ### Data preprocessing ###
    print("Processing market data...")
    rdata['Ticker'] = rdata['Ticker-Region'].dropna().apply(lambda x: x.split('-')[0].strip())
    rdata['Year'] = pd.to_datetime(rdata['Date']).dt.year
    rdata = rdata[['Ticker', 'Ending Price', 'Year', '6-Mo Momentum %']]

    ### Rebalancing portfolio across years ###
    print("Rebalancing portfolio...")
    final_portfolio = rebalance_portfolio(rdata, start_year=2002, end_year=2023, initial_aum=1)

if __name__ == "__main__":
    main()
