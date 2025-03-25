import matplotlib.pyplot as plt
from MarketObject import MarketObject
from FactorFunction import Factors
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
    holdings = {}
    equal_investment = aum / len(top_10_percent)

    for ticker, _ in top_10_percent:
        price = market.getPrice(ticker)
        if price is not None and price > 0:
            holdings[ticker] = equal_investment / price

    return holdings

def calculate_growth(portfolio, start_year, end_year, next_market, current_market):
    # Calculate start value using the current market
    total_start_value = sum(
        portfolio[ticker] * current_market.getPrice(ticker)
        for ticker in portfolio if current_market.getPrice(ticker) is not None
    )

    # Calculate end value using next market, handling missing stocks
    total_end_value = 0
    for ticker in portfolio:
        end_price = next_market.getPrice(ticker)
        if end_price is not None:
            # Use next year's price for growth calculation
            total_end_value += portfolio[ticker] * end_price
        else:
            # Stock missing in next market, liquidate at entry price
            entry_price = current_market.getPrice(ticker)
            if entry_price is not None:
                total_end_value += portfolio[ticker] * entry_price
                print(f"{ticker} - Missing in {end_year}, liquidating at entry price: {entry_price}")

    # Calculate growth
    growth = (total_end_value - total_start_value) / total_start_value if total_start_value else 0
    return growth, total_start_value, total_end_value

def rebalance_portfolio(data, start_year, end_year, initial_aum):
    aum = initial_aum
    portfolio = {}
    years = []
    portfolio_values = []

    for year in range(start_year, end_year + 1):
        print(f"\nRebalancing Portfolio for {year} based on factors...")
        market = MarketObject(data.loc[data['Year']==year], year)

        portfolio_holdings = calculate_holdings(
            aum=aum,
            market=market
        )
        
        # Convert holdings dictionary into investments for Portfolio
        portfolio[f"Portfolio_{year}"] = [{'ticker': ticker, 'number_of_shares': shares} for ticker, shares in portfolio_holdings.items()]
        # Convert the portfolio for the current year back to the expected format
        formatted_portfolio = {inv['ticker']: inv['number_of_shares'] for inv in portfolio[f"Portfolio_{year}"]}

        if market.t < end_year:
            next_market = MarketObject(data.loc[data['Year'] == year +1], year+1)
            growth, total_start_value, total_end_value = calculate_growth(formatted_portfolio, year, year + 1, next_market, market)
            print(f"Year {year} to {year+1}: Growth: {growth:.2%}, Start Value: ${total_start_value:.2f}, End Value: ${total_end_value:.2f}")
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
    plt.xlabel("Year")
    plt.ylabel("Portfolio Value ($)")
    plt.title("Portfolio Growth Over Time")
    plt.grid(True)
    plt.legend()
    plt.show()

    return portfolio
