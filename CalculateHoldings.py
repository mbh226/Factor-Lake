import matplotlib.pyplot as plt
from MarketObject import MarketObject
from FactorFunction import Factors
from portfolio import Portfolio
import pandas as pd
import numpy as np

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
    years = []
    portfolio_returns = []  # Store yearly returns for Information Ratio
    benchmark_returns = []  # Store benchmark returns for comparison

    for year in range(start_year, end_year):
        print(f"\nRebalancing Portfolio for {year} based on factors...")
        market = MarketObject(data.loc[data['Year'] == year], year)
        
        yearly_portfolio = calculate_holdings(
            aum=aum,
            market=market
        )
        
        if year < end_year:
            next_market = MarketObject(data.loc[data['Year'] == year + 1], year + 1)
            growth, total_start_value, total_end_value = calculate_growth(yearly_portfolio, next_market, market)
            
            print(f"Year {year} to {year + 1}: Growth: {growth:.2%}, Start Value: ${total_start_value:.2f}, End Value: ${total_end_value:.2f}")
            aum = total_end_value  # Liquidate and reinvest
            
            # Append annual return (growth) to portfolio_returns
            portfolio_returns.append(growth)

            # Get benchmark return for the year (replace it as needed)
            benchmark_return = get_benchmark_return(year)  # Define this function based on benchmark data
            benchmark_returns.append(benchmark_return)

        years.append(year)

    # Calculate overall growth
    overall_growth = (aum - initial_aum) / initial_aum if initial_aum else 0
    print(f"\nFinal Portfolio Value after {end_year}: ${aum:.2f}")
    print(f"Overall Growth from {start_year} to {end_year}: {overall_growth * 100:.2f}%")
    
    # Calculate and print Information Ratio
    information_ratio = calculate_information_ratio(portfolio_returns, benchmark_returns)
    if information_ratio is not None:
        print(f"Information Ratio: {information_ratio:.4f}")
    else:
        print("Information Ratio could not be calculated due to zero tracking error.")
    
    return portfolio_returns, benchmark_returns, aum

def get_benchmark_return(year):
    """
    This function should return the benchmark return for the given year.
    """
    # Data from Factset (September)
    benchmark_data = {
        2002: 34.62, 2003: 17.48, 2004: 16.56, 2005: 8.65, 2006: 11.01,
        2007: -15.63, 2008: -11.08, 2009: 11.89, 2010: -4.73, 2011: 30.01,
        2012: 28.22, 2013: 2.6, 2014: -0.09, 2015: 13.71, 2016: 19.11,
        2017: 13.8, 2018: -10.21, 2019: -1.03, 2020: 46.21, 2021: -24.48, 2022: 7.23
    }
    return benchmark_data.get(year, 0)

def calculate_information_ratio(portfolio_returns, benchmark_returns):
    """
    Calculates the Information Ratio (IR) for a given set of portfolio returns and benchmark returns.
    
    Parameters:
        portfolio_returns (list or np.array): List of portfolio returns over time.
        benchmark_returns (list or np.array): List of benchmark returns over time.
    
    Returns:
        float: The Information Ratio value.
    """
    # Ensure inputs are numpy arrays for mathematical operations
    portfolio_returns = np.array(portfolio_returns)
    benchmark_returns = np.array(benchmark_returns)

    # Calculate active returns
    active_returns = portfolio_returns - benchmark_returns
    
    # Calculate the mean active return (numerator)
    mean_active_return = np.mean(active_returns)
    
    # Calculate tracking error (denominator)
    tracking_error = np.std(active_returns, ddof=1)  # Use sample std deviation

    # Prevent division by zero
    if tracking_error == 0:
        return None  # Or return float('nan') to indicate undefined IR
    
    # Compute Information Ratio
    information_ratio = mean_active_return / tracking_error
    return information_ratio
