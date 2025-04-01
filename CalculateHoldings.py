import matplotlib.pyplot as plt
from MarketObject import MarketObject
from FactorFunction import Factors
from portfolio import Portfolio
import pandas as pd

def calculate_holdings(aum, market):
    # Factor values for all tickers in the market
    factor_values = {ticker: Factors.Momentum6m(ticker, market) for ticker in market.stocks['Ticker']}
    
    # Remove None values from factor_values
    factor_values = {ticker: value for ticker, value in factor_values.items() if value is not None}

    # Sort securities by factor values in descending order
    sorted_securities = sorted(factor_values.items(), key=lambda x: x[1], reverse=True)

    # Select the top 10% of securities
    top_10_percent = sorted_securities[:max(1, len(sorted_securities) // 10)]

    # Calculate number of shares for each selected security
    portfolio_new = Portfolio(name=f"Portfolio_{market.t}")
    equal_investment = aum / len(top_10_percent)

    for ticker, _ in top_10_percent:
        price = market.getPrice(ticker)
        if price is not None and price > 0:
            shares = equal_investment / price
            portfolio_new.add_investment(ticker, shares)

    return portfolio_new

def calculate_growth(portfolio, next_market, current_market):
    # Calculate start value using the current market
    total_start_value = portfolio.present_value(current_market)

    # Calculate end value using next market, handling missing stocks
    total_end_value = 0
    for inv in portfolio.investments:
        ticker = inv["ticker"]
        end_price = next_market.getPrice(ticker)
        if end_price is not None:
            # Use next year's price for growth calculation
            total_end_value += inv["number_of_shares"] * end_price
        else:
            # Stock missing in next market, liquidate at entry price
            entry_price = current_market.getPrice(ticker)
            if entry_price is not None:
                total_end_value += inv["number_of_shares"] * entry_price
                print(f"{ticker} - Missing in {next_market.t}, liquidating at entry price: {entry_price}")

    # Calculate growth
    growth = (total_end_value - total_start_value) / total_start_value if total_start_value else 0
    return growth, total_start_value, total_end_value

def rebalance_portfolio(data, start_year, end_year, initial_aum):
    aum = initial_aum
    initial_portfolio = Portfolio(name="Initial Portfolio")
    years = []
    portfolio_values = []

    for year in range(start_year, end_year + 1):
        print(f"\nRebalancing Portfolio for {year} based on factors...")
        market = MarketObject(data.loc[data['Year'] == year], year)
        
        yearly_portfolio = calculate_holdings(
            aum=aum,
            market=market
        )
        
        if market.t < end_year:
            next_market = MarketObject(data.loc[data['Year'] == year + 1], year + 1)
            growth, total_start_value, total_end_value = calculate_growth(yearly_portfolio, next_market, market)
            print(f"Year {year} to {year + 1}: Growth: {growth:.2%}, Start Value: ${total_start_value:.2f}, End Value: ${total_end_value:.2f}")
            aum = total_end_value  # Liquidate and reinvest
        
        # Track values for plotting
        years.append(year)
        portfolio_values.append(aum)

    # Calculate overall growth
    overall_growth = (aum - initial_aum) / initial_aum if initial_aum else 0
    print(f"\nFinal Portfolio Value after {end_year}: ${aum:.2f}")
    print(f"Overall Growth from {start_year} to {end_year}: {overall_growth * 100:.2f}%")

    # Plot the portfolio value over time
    plt.figure(figsize=(10, 5))
    plt.plot(years, portfolio_values, marker='o', linestyle='-', color='b', label='Portfolio Value')
    plt.xticks(years, rotation=45)  # Ensures all years are displayed properly
    plt.xlabel("Year")
    plt.ylabel("Portfolio Value ($)")
    plt.title("Portfolio Growth Over Time")
    plt.grid(True)
    plt.legend()
    plt.show()
    
    return portfolio_values