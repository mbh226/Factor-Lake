# Read data sheets
data = pd.read_excel(file_path, sheet_name='Data', header=2)

"""Factor selection"""

# Define possible factors with numbers
factors = {
    1: '12-Mo Momentum %',
    2: '6-Mo Momentum %',
    3: '1-Mo Momentum %',
    4: '1-Yr Price Vol %',
    5: 'Accruals/Assets',
    6: 'ROA %',
    7: '1-Yr Asset Growth %',
    8: '1-Yr CapEX Growth %',
    9: 'Book/Price',
    10: "Next-Year's Return %",
    11: "Next-Year's Active Return %",
    12: 'ROE using 9/30 Data',
    13: 'ROA using 9/30 Data',
    14: 'Price to Book Using 9/30 Data'
}

# Display numbered factors
print("Available factors:")
for num, factor in factors.items():
    print(f"{num}: {factor}")

# Get the number of factors to use
factor_number = int(input("How many factors do you want to use? "))

# Get user-selected factors by number
factor_set = []
for i in range(factor_number):
    while True:
        try:
            user_choice = int(input(f"Enter factor number ({i+1}/{factor_number}): "))
            if user_choice in factors:
                factor_set.append(factors[user_choice])
                break
            else:
                print("Invalid number. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

print("\nSelected factors:")
for factor in factor_set:
    print(factor)

"""Construct Portfolio"""
#set chosen factor columns
# Replace '--' with NaN
data.replace('--', np.nan, inplace=True)
data = data[['Date', 'Security Name', 'Ending Price', 'Russell 2000 Port. Weight'] + factor_set]  # Select relevant columns

# Normalize the factors
for factor in factor_set:
    data[factor] = (data[factor] - data[factor].mean()) / data[factor].std()

# Assign weights to the factors (equal weights)
weights = np.ones(len(factor_set)) / len(factor_set)

# Calculate the weighted sum of factors
data['Portfolio'] = data[factor_set].dot(weights)
data = data.dropna(subset=['Portfolio'])
portfolio = data[['Security Name', 'Date', 'Portfolio']]

#Sorts Portfolio weights by year and gives the average portfolio weight for a given year
data['Year'] = pd.to_datetime(data['Date']).dt.year
data['Yearly Portfolio'] = data.groupby('Year')['Portfolio'].transform('mean')
yearly_portfolio = data[['Year', 'Yearly Portfolio']].drop_duplicates()

# Display the constructed portfolio weights
print("\nConstructed Portfolio")
print(portfolio)

# Display the yearly portfolio weights
print("\nYearly Portfolio Weights")
print(yearly_portfolio)

# get price data
price_data = data.pivot_table(index = 'Security Name', columns = 'Year', values = 'Ending Price')
price_data.columns.name = None
# print(price_data)

# get weight data
weight_data = data.pivot_table(index = 'Security Name', columns = 'Year', values = 'Portfolio')
weight_data.columns.name = None
# print(weight_data)

# calculate portfolio return
portfolios_return = {}
for year in range(2002, 2023):
    stocks_return = (price_data[year + 1] - price_data[year]) / price_data[year]
    portfolios_return[year] = (stocks_return * weight_data[year]).sum()

for year in range(2002, 2023):
    print(f"Year {year}: Portfolio Return = {portfolios_return[year]}")

# calculate benchmark returns

# getting benchmark ending price data
benchmark_price_data = data.pivot_table(index='Security Name', columns='Year', values='Ending Price')
benchmark_price_data.columns.name = None

# getting benchmark weight data
benchmark_weight_data = data.pivot_table(index='Security Name', columns='Year', values='Russell 2000 Port. Weight')
benchmark_weight_data.columns.name = None


benchmark_returns = {}
for year in range(2003, 2023):
    # calculate stock returns for the current year using benchmark_price_data
    benchmark_stocks_return = (benchmark_price_data[year + 1] - benchmark_price_data[year]) / benchmark_price_data[year]

    # calculate weighted benchmark for loop's current year
    weighted_benchmark = ((benchmark_stocks_return * benchmark_weight_data[year]).sum())
    benchmark_returns[year] = weighted_benchmark

# print the benchmark returns for each year
for year in range(2003, 2023):
    print(f"Year {year}: Benchmark Return = {benchmark_returns[year]}")

# calculate information ratio

excess_returns = []
for year in range(2003, 2023):
    excess_return = portfolios_return[year] - benchmark_returns[year]

    excess_returns.append(excess_return)

mean_excess_return = np.mean(excess_returns)
tracking_error = np.std(excess_returns)

information_ratio = mean_excess_return / tracking_error
print(f"Portfolio excess return: {mean_excess_return}")
print(f"Portfolio tracking error: {tracking_error}")
print(f"Portfolio Information Ratio: {information_ratio}")
