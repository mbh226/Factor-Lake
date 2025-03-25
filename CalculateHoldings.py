from MarketObject import MarketObject
from FactorFunction import Factors
from portfolio import Portfolio
import pandas as pd

def calculate_holdings(aum, market):
    # Factor values for all tickers in the market
    factor_values = {ticker: Factors.Momentum6m(ticker, market) for ticker in market.stocks['Ticker']}

    # Sort securities by factor values in descending order
    sorted_securities = sorted(factor_values.items(), key=lambda x: x[1], reverse=True)

    # Select the top 10% of securities
    top_10_percent = sorted_securities[:max(1, len(sorted_securities) // 10)]

    # Calculate number of shares for each selected security
    holdings = {}
    equal_investment = aum / len(top_10_percent)

    for ticker, _ in top_10_percent:
        price = market.getPrice(ticker)
        if price is not None and price > 0:
            holdings[ticker] = equal_investment / price

    return holdings

def calculate_growth(portfolio, start_year, end_year, market):
    # Calculate growth using the market object for price retrieval
    total_start_value = sum(portfolio[ticker] * market.getPrice(ticker) for ticker in portfolio if market.getPrice(ticker) is not None)
    total_end_value = sum(portfolio[ticker] * market.getPrice(ticker) for ticker in portfolio if market.getPrice(ticker) is not None)

    # Handle removed stocks
    removed_stocks = [ticker for ticker in portfolio if market.getPrice(ticker) is None]
    liquidated_value = sum(portfolio[ticker] * market.getPrice(ticker) for ticker in removed_stocks if market.getPrice(ticker) is not None)
    total_end_value += liquidated_value

    # Calculate growth
    growth = (total_end_value - total_start_value) / total_start_value if total_start_value else 0
    return growth, total_start_value, total_end_value

def rebalance_portfolio(data, start_year, end_year, initial_aum):
    aum = initial_aum
    portfolio = {}

    for year in range(start_year, end_year + 1):
        print(f"\nRebalancing Portfolio for {year} based on factors...")
        market = MarketObject(data.loc[data['Year']==year], year)

        portfolio_holdings = calculate_holdings(
            aum=aum,
            market=market
        )
        
        # Convert holdings dictionary into investments for Portfolio
        invest = [{'ticker': ticker, 'number_of_shares': shares} for ticker, shares in portfolio_holdings.items()]
        portfolio = Portfolio(name=f"Portfolio_{year}", investments=invest)
        
        if market.t < end_year:
            next_market = MarketObject(data.loc[data['Year'] == year +1], year+1)
            growth, start_value, end_value = calculate_growth(data, portfolio, year, year + 1, market)
            print(f"Year {year} to {year+1}: Growth: {growth:.2%}, Start Value: ${start_value:.2f}, End Value: ${end_value:.2f}")
            aum = end_value  # Liquidate and reinvest

    # Calculate overall growth
    overall_growth = (aum - initial_aum) / initial_aum if initial_aum else 0
    print(f"\nFinal Portfolio Value after {end_year}: ${aum:.2f}")
    print(f"Overall Growth from {start_year} to {end_year}: {overall_growth:.2f}%")

    return portfolio



