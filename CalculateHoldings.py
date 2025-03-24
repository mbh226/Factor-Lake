
def rebalance_portfolio(data, factor_name, start_year, end_year, initial_aum):
    data = data.copy()
    data['Year'] = pd.to_datetime(data['Date']).dt.year
    aum = initial_aum
    portfolio = {}

    for year in range(start_year, end_year + 1):
        print(f"\nRebalancing Portfolio for {year} based on {factor_name}...")
        portfolio = build_factor_portfolio(data, factor_name, year, aum)

        if year < end_year:
            market = MarketObject(data.loc[data['Year'] == year], year)
            growth, start_value, end_value = calculate_growth(data, portfolio, year, year + 1, market)
            print(f"Year {year} to {year+1}: Growth: {growth:.2%}, Start Value: ${start_value:.2f}, End Value: ${end_value:.2f}")
            aum = end_value  # Liquidate and reinvest

    overall_growth = (aum - initial_aum) / initial_aum if initial_aum else 0
    print(f"Final Portfolio Value after {end_year}: ${aum:.2f}")
    print(f"Overall Growth from {start_year} to {end_year}: {overall_growth:.2%}")

    return portfolio