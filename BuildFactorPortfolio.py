def build_factor_portfolio(data, factor_name, date, aum, top_percent=0.1):
    data = data.copy()
    data['Year'] = pd.to_datetime(data['Date']).dt.year
    factor_data = data.loc[data['Year'] == date, ['Ticker-Region', 'Ending Price', factor_name]].dropna()

    if factor_data.empty:
        print(f"No data available for factor {factor_name} in {date}")
        return {}

    factor_data['Factor Score'] = factor_data[factor_name].rank(pct=True)
    top_stocks = factor_data.nlargest(int(len(factor_data) * top_percent), 'Factor Score')

    num_stocks = len(top_stocks)
    allocation_per_stock = aum / num_stocks if num_stocks > 0 else 0

    top_stocks['Shares'] = allocation_per_stock / top_stocks['Ending Price']

    return top_stocks.set_index('Ticker-Region')['Shares'].to_dict()
