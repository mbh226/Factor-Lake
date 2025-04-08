# Imports
import pandas as pd
import json

# FDS Packages 
import fds.sdk.FactSetPrices  # To install: "pip install fds.sdk.utils fds.sdk.FactSetPrices==1.1.7"
from fds.sdk.FactSetPrices.api import prices_api
from fds.sdk.FactSetPrices.models import *
from fds.sdk.utils.authentication import ConfidentialClient

# Path to configuration file
config_file_path = '/content/factor-lake/FactSet_Colab_Test-config.json'

# Load credentials
with open(config_file_path, "r") as config_file:
    config_data = json.load(config_file)

#Authentication
configuration = fds.sdk.FactSetPrices.Configuration(
    fds_oauth_client=ConfidentialClient(
        client_id=config_data["clientId"],
        client_auth_type=config_data["clientAuthType"],
        base_url="https://api.factset.com/content"  # Explicitly set the production server
    )
)


# Get fixed-income data
with fds.sdk.FactSetPrices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prices_api.PricesApi(api_client)

    prices_fixed_income_request = PricesFixedIncomeRequest(
        ids=FixedIds(["037833BX"]),  # Replace with valid security IDs
        start_date="2019-01-01",     # Replace with desired start date
        end_date="2019-12-31",       # Replace with desired end date
        frequency=FrequencyFi("M"),  # Frequency: "M" for monthly
    )

    # Send Request
    try:
        api_response = api_instance.get_fixed_security_prices_for_list(prices_fixed_income_request)
        # Convert to Pandas DataFrame
        results = pd.json_normalize([a.__dict__["_data_store"] for a in api_response["data"]])
        print(results)
    except Exception as e:
        print(f"An error occurred: {e}")
