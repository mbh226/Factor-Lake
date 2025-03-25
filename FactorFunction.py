from MarketObject import MarketObject, load_data
import pandas as pd

class Factors:
    @staticmethod
    def Momentum6m(ticker, market):
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


#Creating an Example
if __name__ == "__main__":
    rdata = load_data()
    rdata.columns = rdata.columns.str.strip()
    rdata = rdata.loc[:, ~rdata.columns.duplicated(keep='first')]
    rdata['Ticker'] = rdata['Ticker-Region'].dropna().apply(lambda x: x.split('-')[0].strip())
    rdata['Date'] = pd.to_datetime(rdata['Date'])
    rdata['Year'] = rdata['Date'].dt.year

    df_2002 = rdata[rdata['Year'] == 2002].copy()
    df_2003 = rdata[rdata['Year'] == 2003].copy()

    marketObject_2002 = MarketObject(df_2002, 2002)
    marketObject_2003 = MarketObject(df_2003, 2003)


    # EXAMPLE USING Factors CLASS 
    Momentum6m_2002_FLWS = Factors.Momentum6m("FLWS", marketObject_2002)
    Momentum6m_2002_AAPL = Factors.Momentum6m("AAPL", marketObject_2002)

    print(f'\n6 Month Momentum Value of FLWS in 2002: ' + str(Momentum6m_2002_FLWS))
    print(f'6 Month Momentum Value of AAPL in 2002: ' + str(Momentum6m_2002_AAPL))

