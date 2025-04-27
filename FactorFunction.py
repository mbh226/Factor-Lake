from MarketObject import load_data

load_data
class Factors:
    def get(ticker, market):
        return "Factor not specified"

class Momentum6m(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['6-Mo Momentum %'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing 6-Mo Momentum % for {ticker}: {e}")
            return None
        
class Momentum12m(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['12-Mo Momentum %'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing 12-Mo Momentum % for {ticker}: {e}")
            return None
        
class Momentum1m(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['1-Mo Momentum %'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing 1-Mo Momentum % for {ticker}: {e}")
            return None

class ROE(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['ROE using 9/30 Data'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing 6-Mo Momentum % for {ticker}: {e}")
            return None

class ROA(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['ROA using 9/30 Data'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing 6-Mo Momentum % for {ticker}: {e}")
            return None
        
class P2B(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['Price to Book Using 9/30 Data'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing Price to Book Using 9/30 Data for {ticker}: {e}")
            return None
        
class NextFYrEarns(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['Next FY Earns/P'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing Next FY Earns/P for {ticker}: {e}")
            return None
        
class OneYrPriceVol(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['1-Yr Price Vol %'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing 1-Yr Price Vol % for {ticker}: {e}")
            return None
        
class AccrualsAssets(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['Accruals/Assets'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing Accruals/Assets % for {ticker}: {e}")
            return None
        
class ROAPercentage(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['ROA %'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing ROA % for {ticker}: {e}")
            return None
        
class OneYrAssetGrowth(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['1-Yr Asset Growth %'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing 1-Yr Asset Growth % for {ticker}: {e}")
            return None
        
class OneYrCapEXGrowth(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['1-Yr CapEX Growth %'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing 1-Yr CapEX Growth % for {ticker}: {e}")
            return None
        
class BookPrice(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['Book/Price'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing Book/Price for {ticker}: {e}")
            return None
        
class NextYrReturn(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['Next-Year\'s Return %'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing Next-Year's Return % for {ticker}: {e}")
            return None
        
class NextYrActiveReturn(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['Next-Year\'s Active Return %'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            print(f"Error accessing Next-Year's Active Return % for {ticker}: {e}")
            return None

# #Creating an Example
# if __name__ == "__main__":
#     rdata = load_data()
#     rdata.columns = rdata.columns.str.strip()
#     rdata = rdata.loc[:, ~rdata.columns.duplicated(keep='first')]
#     rdata['Ticker'] = rdata['Ticker-Region'].dropna().apply(lambda x: x.split('-')[0].strip())
#     rdata['Date'] = pd.to_datetime(rdata['Date'])
#     rdata['Year'] = rdata['Date'].dt.year

#     df_2002 = rdata[rdata['Year'] == 2002].copy()
#     df_2003 = rdata[rdata['Year'] == 2003].copy()

#     marketObject_2002 = MarketObject(df_2002, 2002)
#     marketObject_2003 = MarketObject(df_2003, 2003)


#     # EXAMPLE USING Factors CLASS 
#     Momentum6m_2002_FLWS = Factors.Momentum6m("FLWS", marketObject_2002)
#     Momentum6m_2002_AAPL = Factors.Momentum6m("AAPL", marketObject_2002)

#     print(f'\n6 Month Momentum Value of FLWS in 2002: ' + str(Momentum6m_2002_FLWS))
#     print(f'6 Month Momentum Value of AAPL in 2002: ' + str(Momentum6m_2002_AAPL))

