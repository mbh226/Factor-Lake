import sys
import os

#adding the project directory to sys.path so it can appropriately import portfolio and market objects
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from portfolio import Portfolio, factor_lake_return
from MarketObject import MarketObject, load_data
import unittest
import pandas as pd

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        rdata = load_data()
        data = rdata.copy()
        #split ticker-region at the dash and take the ticker
        data['Ticker'] = data['Ticker-Region'].dropna().str.split('-').str[0]
        data['Year'] = pd.to_datetime(data['Date']).dt.year
        data = data[['Ticker', 'Ending Price', 'Year', '6-Mo Momentum %']]

        #initialize market objects
        self.marketObject_2002 = MarketObject(data.loc[data['Year'] == 2002],2002)
        self.marketObject_2023 = MarketObject(data.loc[data['Year'] == 2023],2023)

        #initialize portfolio and add investments
        self.portfolio = Portfolio('FACTOR LAKE PORTFOLIO')
        self.portfolio.add_investment("AOS", 50)
        self.portfolio.add_investment("AAPL", 10)

    def test_portfolio(self):
        expected_final_value = 4.39
        expected_growth = 339.42

        value_2002 = self.portfolio.present_value(self.marketObject_2002)
        value_2023 = self.portfolio.present_value(self.marketObject_2023)

        factor_lake_return = self.portfolio.calculate_return(value_2002, value_2023)

        #acceptable margins for error
        final_value_tolerance = 0.01
        growth_tolerance = 0.1

        self.assertAlmostEqual(value_2023, expected_final_value, delta=final_value_tolerance)
        self.assertAlmostEqual(factor_lake_return, expected_growth, delta=growth_tolerance)

if __name__ == '__main__':
    unittest.main()
