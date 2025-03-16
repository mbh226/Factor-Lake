### HYPOTHETICALLY IMPORTING MARKET CLASS FROM market.py ###
from market import Market

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
        return (t2_value - t1_value) / t1_value * 100

### EXAMPLE USING PORTFOLIO CLASS ###
portfolio = Portfolio('FACTOR LAKE PORTFOLIO')

portfolio.add_investment("AAPL", 50)
portfolio.add_investment("GOOG", 20)

### MARKET DATA ###
t1_price = Market({"AAPL": 150, "GOOG": 2700})
t2_price = Market({"AAPL": 160, "GOOG": 2800})

## PORTFOLIO VALUE CALCULATION ###
value_t1 = portfolio.present_value(t1_price)
value_t2 = portfolio.present_value(t2_price)

factor_lake_return = portfolio.calculate_return(value_t1,value_t2)

print(f'Portfolio Value at T1: ${value_t1:.2f}')
print(f'Portfolio Value at T2: ${value_t2:.2f}')
print(f'Portfolio Return: {factor_lake_return:.2f}%')