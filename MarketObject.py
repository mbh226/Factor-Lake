import pandas as pd
import numpy as np
### CREATING FUNCTION TO LOAD DATA ###
def load_data():
    file_path = 'C:\\Users\\FM\'s Laptop\\Downloads\\College\\SYSEN 5900-669\\Financial Portfoilio\\Clean output\\FR2000 Annual Quant Data FOR RETURN SIMULATION.xlsx'
    rdata = pd.read_excel(file_path, sheet_name='Data', header=2, skiprows=[3, 4])
    return rdata

class MarketObject():
    def __init__(self, data, t, verbosity=1):
        """
        data(DataFrame): column 1 is 'Ticker', column 2 is 'Ending Price', column 3 is 'Year', column 4 is 'ROE using 9/30 Data', etc.
        t (int): Year of market data.
        verbosity (int): Controls level of printed output. 0 = silent, 1 = normal, 2+ = verbose.
        """
        data.columns = data.columns.str.strip()
        data = data.loc[:, ~data.columns.duplicated(keep='first')]

        if 'Ticker' not in data.columns and 'Ticker-Region' in data.columns:
            data['Ticker'] = data['Ticker-Region'].dropna().apply(lambda x: x.split('-')[0].strip())
        if 'Year' not in data.columns and 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'])
            data['Year'] = data['Date'].dt.year

        available_factors = [
            'ROE using 9/30 Data', 'ROA using 9/30 Data', '12-Mo Momentum %', '1-Mo Momentum %',
            'Price to Book Using 9/30 Data', 'Next FY Earns/P', '1-Yr Price Vol %', 'Accruals/Assets',
            'ROA %', '1-Yr Asset Growth %', '1-Yr CapEX Growth %', 'Book/Price',
            "Next-Year's Return %", "Next-Year's Active Return %"
        ]

        keep_cols = ['Ticker', 'Ending Price', 'Year', '6-Mo Momentum %'] + available_factors
        data = data[[col for col in keep_cols if col in data.columns]].copy()

        # Replace '--' with NaNs
        data[['Ending Price'] + available_factors] = data[['Ending Price'] + available_factors].replace('--', None)

        self.stocks = data
        self.t = t
        self.verbosity = verbosity

    def getPrice(self, ticker):
        ticker_data = self.stocks.loc[self.stocks['Ticker'] == ticker]
        if ticker_data.empty:
            if self.verbosity >= 2:
                print(f"{ticker} - not found in market data for {self.t} - SKIPPING")
            return None
        return ticker_data['Ending Price'].iloc[-1]
