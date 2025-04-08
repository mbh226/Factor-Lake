# Imports
import pandas as pd
import json

# FDS Packages
from fds.sdk.utils.authentication import ConfidentialClient
import fds.sdk.OverviewReportBuilder
from fds.sdk.OverviewReportBuilder.api import company_api
from fds.sdk.OverviewReportBuilder.models import *
from pprint import pprint

# Path to configuration file
config_file_path = '/content/factor-lake/FactSet_Colab_Test-config.json'

# Authentication
configuration = fds.sdk.OverviewReportBuilder.Configuration(
    fds_oauth_client=ConfidentialClient(config_file_path)
)

# Retrieve company data
with fds.sdk.OverviewReportBuilder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = company_api.CompanyApi(api_client)
    id = "FDS"  # Replace with valid company ticker

    try:
        # Fetch current capitalization
        api_response = api_instance.get_current_cap(id)

        # Convert API response to Pandas DataFrame
        response_dict = api_response.to_dict()['data']
        simple_json_response = pd.DataFrame(response_dict)
        nested_json_response = pd.json_normalize(response_dict)

        # Print the DataFrames
        print("Simple JSON Response:")
        print(simple_json_response)
        print("\nNested JSON Response:")
        print(nested_json_response)
    except fds.sdk.OverviewReportBuilder.ApiException as e:
        print(f"Exception when calling CompanyApi->get_current_cap: {e}")
