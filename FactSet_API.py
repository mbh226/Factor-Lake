# Imports
import pandas as pd
import json

# FDS Packages 
import fds.sdk.FactSetPrices # To install, please use "pip install fds.sdk.utils fds.sdk.FactSetPrices==1.1.7"
from fds.sdk.FactSetPrices.api import prices_api, returns_api, dividends_api, splits_api, shares_api, market_value_api, high_low_api, database_rollover_api
from fds.sdk.FactSetPrices.models import *
from fds.sdk.utils.authentication import ConfidentialClient

# Load credentials from the JSON file
with open("FactSet_Colab_Test-config.json") as config_file:
    config_data = json.load(config_file)

# Authentication
configuration = fds.sdk.FactSetPrices.Configuration(
    fds_oauth_client=ConfidentialClient(
        client_id=config_data["client_id"],
        client_secret=config_data["client_secret"],
        base_url=config_data["base_url"]
    )
)

# Get fixed-income data
with fds.sdk.FactSetPrices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prices_api.PricesApi(api_client)

    prices_fixed_income_request = PricesFixedIncomeRequest(
        ids=FixedIds(["037833BX"]),
        start_date="2019-01-01",
        end_date="2019-12-31",
        frequency=FrequencyFi("M"),
    ) 
    
    # Send Request
    api_response = api_instance.get_fixed_security_prices_for_list(prices_fixed_income_request)

    # Convert to Pandas Dataframe
    results = pd.json_normalize([a.__dict__["_data_store"] for a in api_response["data"]])
    print(results)
