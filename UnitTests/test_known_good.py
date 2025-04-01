import sys
import os

#adding the project directory to sys.path so it can appropriately import portfolio and market objects
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from FactorFunction import Factors
from MarketObject import MarketObject, load_data
from portfolio import rebalance_portfolio
import unittest
import pandas as pd

class TestFactorLakePortfolio(unittest.TestCase):
    def setUp(self):
        self.data = load_data()
        self.data.columns = self.data.columns.str.strip()
        self.data = self.data.loc[:, ~self.data.columns.duplicated(keep='first')]
        #split ticker-region at the dash and take the ticker
        self.data['Ticker'] = self.data['Ticker-Region'].dropna().str.split('-').str[0]
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data['Year'] = self.data(['Date']).dt.year

    def test_portfolio_growth(self):
        initial_aum = 1
        start_year = 2002
        end_year = 2023

        portfolio = rebalance_portfolio(self.data, start_year, end_year, initial_aum)

        expected_final_value = 4.39
        expected_growth = 339.42

        self.assertAlmostEqual(portfolio[-1]['aum'], expected_final_value, delta=0.01,
                               msg=f'Expected final portfolio value: {expected_final_value}, but got {portfolio[-1]["aum"]}')

        overall_growth = (portfolio[-1]['aum'] - initial_aum) / initial_aum * 100
        self.assertAlmostEqual(overall_growth, expected_growth, delta=0.1,
                               msg=f'Expected overall growth: {expected_growth}%, but got {overall_growth}%')

if __name__ == '__main__':
    unittest.main()
