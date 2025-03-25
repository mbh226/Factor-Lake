import pytest
import json
import numpy
import pandas as pd
from CalculateHoldings import rebalance_portfolio

@pytest.fixture
def market_data():
    return pd.read_pickle('UnitTests/test_data.pkl')

@pytest.fixture
def rebalanced_portfolio_data():
    with open('UnitTests/test_rebalanced_portfolio.json', 'r') as f:
        return json.load(f)

def test_rebalance_portfolio(market_data, rebalanced_portfolio_data):
    """
    Test the rebalance_portfolio function
    """

    market_data['Ticker'] = market_data['Ticker-Region'].dropna().apply(lambda x: x[0:x.find('-')])
    market_data['Year'] = pd.to_datetime(market_data['Date']).dt.year
    market_data = market_data[['Ticker', 'Ending Price', 'Year', '6-Mo Momentum %']]

    rebalanced_portfolio = rebalance_portfolio(market_data, start_year=2002, end_year=2023, initial_aum=1)
    assert rebalanced_portfolio == rebalanced_portfolio_data, \
        f"Test failed: The rebalanced portfolios is not equal the expected portfolios."
