### HYPOTHETICALLY IMPORTING MARKET CLASS FROM market.py ###
from MarketObject import MarketObject

class Portfolio:
    ### INITIALIZE PORTFOLIO BY PROVIDING A NAME AND A LIST OF INVESTMENTS ###
    def __init__(self, name, investments=None):
        self.name = name
        if investments is not None:
            self.investments = investments
        else:
            self.investments = []

    ### ADDING STOCK TO PORTFOLIO ###
    def add_investment(self, ticker, nShares):
        investment = {'ticker': ticker, 'number_of_shares': nShares}
        self.investments.append(investment)

    ### REMOVE STOCK FROM PORTFOLIO ###
    def remove_investment(self, ticker):
        investment_list = []
        for inv in self.investments:
            if inv['ticker'] != ticker:
                investment_list.append(inv)
        ### UPDATE PORTFOLIO INVESTMENTS LIST AFTER REMOVING STOCKS ###
        self.investments = investment_list

    ### CALCULATE PORTFOLIO VALUE ###
    def present_value(self, market):
        total_value = 0
        for inv in self.investments:
            ### HYPOTHETICAL GET_PRICE METHOD FROM MARKET CLASS FOR EACH STOCK ###
            price = market.get_price(inv["ticker"])
            total_value += price * inv["number_of_shares"]
        return total_value

    def calculate_return(self, t1_value, t2_value):
        if t1 !=0:
            return (t2_value - t1_value) / t1_value * 100
        else:
            raise ValueError("Value at time 1 is 0")

### USING PORTFOLIO WITH MARKET OBJECT ###
rdata = load_data()
data = rdata.copy()
data['Ticker'] = data['Ticker-Region'].dropna().apply(lambda x: x[0:x.find('-')])
data['Year'] = pd.to_datetime(data['Date']).dt.year
data = data[['Ticker', 'Ending Price', 'Year']]

marketObject_2002 = MarketObject(data.loc[data['Year'] == 2002], 2002)
marketObject_2003 = MarketObject(data.loc[data['Year'] == 2003], 2003)

### EXAMPLE USING PORTFOLIO CLASS ###
portfolio = Portfolio('FACTOR LAKE PORTFOLIO')
portfolio.add_investment("AOS", 50)
portfolio.add_investment("AAPL", 10)

## PORTFOLIO VALUE CALCULATION ###
value_t1 = portfolio.present_value(marketObject_2002) #changed t1_price to marketObject_2002
value_t2 = portfolio.present_value(marketObject_2003)#changed t2_price to marketObject_2003

factor_lake_return = portfolio.calculate_return(value_t1,value_t2)

print(f'Portfolio Value in 2002: ${value_t1:.2f}')
print(f'Portfolio Value in 2003: ${value_t2:.2f}')
print(f'Portfolio Return from 2002 to 2003: {factor_lake_return:.2f}%')
