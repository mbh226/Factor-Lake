# Imports
import pandas as pd
import json

# FDS Packages 
import fds.sdk.FactSetPrices # To install, please use "pip install fds.sdk.utils fds.sdk.FactSetPrices==1.1.7"
from fds.sdk.FactSetPrices.api import prices_api, returns_api, dividends_api, splits_api, shares_api, market_value_api, high_low_api, database_rollover_api
from fds.sdk.FactSetPrices.models import *
from fds.sdk.utils.authentication import ConfidentialClient

# Load credentials from the JSON file
# Update the file path to match the cloned Git repository location
config_file_path = "/content/factor-lake/FactSet_Colab_Test-config.json"

with open(config_file_path, "r") as config_file:
    config_data = json.load(config_file)

# Authentication with corrected key names
configuration = fds.sdk.FactSetPrices.Configuration(
    fds_oauth_client=ConfidentialClient(
        client_id=config_data["clientId"],  # Corrected to match JSON key
        client_secret=config_data["clientSecret"],  # Ensure the key name is correct
        base_url=config_data["base_url"]
    )
)

# Get fixed-income data
with fds.sdk.FactSetPrices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prices_api.PricesApi(api_client)

    prices_fixed_income_request = PricesFixedIncomeRequest(
        ids=FixedIds(["037833BX"]),  # Replace with relevant security IDs
        start_date="2019-01-01",     # Replace with desired start date
        end_date="2019-12-31",       # Replace with desired end date
        frequency=FrequencyFi("M"),  # Frequency: "M" for monthly
    ) 
    
    # Send Request
    api_response = api_instance.get_fixed_security_prices_for_list(prices_fixed_income_request)

    # Convert to Pandas Dataframe
    results = pd.json_normalize([a.__dict__["_data_store"] for a in api_response["data"]])
    print(results)
