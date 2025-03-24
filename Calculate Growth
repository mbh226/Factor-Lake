def calculate_growth(data, portfolio, start_year, end_year, market):
    data = data.copy()
    data['Year'] = pd.to_datetime(data['Date']).dt.year
    start_prices = data.loc[data['Year'] == start_year, ['Ticker-Region', 'Ending Price']].set_index('Ticker-Region')
    end_prices = data.loc[data['Year'] == end_year, ['Ticker-Region', 'Ending Price']].set_index('Ticker-Region')

    total_start_value = sum(portfolio[ticker] * start_prices.loc[ticker, 'Ending Price'] for ticker in portfolio if ticker in start_prices.index)
    total_end_value = sum(portfolio[ticker] * end_prices.loc[ticker, 'Ending Price'] for ticker in portfolio if ticker in end_prices.index)

    removed_stocks = [ticker for ticker in portfolio if ticker not in end_prices.index]
    liquidated_value = sum(portfolio[ticker] * start_prices.loc[ticker, 'Ending Price'] for ticker in removed_stocks if ticker in start_prices.index)
    total_end_value += liquidated_value

    growth = (total_end_value - total_start_value) / total_start_value if total_start_value else 0
    return growth, total_start_value, total_end_value
