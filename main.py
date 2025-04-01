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

    ### Example portfolio initialization ###
    print("Initializing portfolio...")
    portfolio = Portfolio('FACTOR LAKE PORTFOLIO')
    portfolio.add_investment("AOS", 50)
    portfolio.add_investment("AAPL", 10)

    ### Calculate portfolio value ###
    market_2002 = MarketObject(rdata[rdata['Year'] == 2002], 2002)
    market_2003 = MarketObject(rdata[rdata['Year'] == 2003], 2003)
    print("Calculating portfolio values...")
    value_t1 = portfolio.present_value(market_2002)
    value_t2 = portfolio.present_value(market_2003)
    portfolio_return = portfolio.calculate_return(value_t1, value_t2)

    print(f'\nPortfolio Value in 2002: ${value_t1:.2f}')
    print(f'Portfolio Value in 2003: ${value_t2:.2f}')
    print(f'Portfolio Return from 2002 to 2003: {portfolio_return:.2f}%')

    ### Rebalancing portfolio across years ###
    print("Rebalancing portfolio...")
    final_portfolio = rebalance_portfolio(rdata, start_year=2002, end_year=2023, initial_aum=1)
    print(f"\nFinal Rebalanced Portfolio: {final_portfolio}")

if __name__ == "__main__":
    main()
