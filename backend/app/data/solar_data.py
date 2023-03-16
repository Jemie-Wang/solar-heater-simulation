import os
import requests
import logging
from utils.config import SOLAR_API

class solar_data:

    def get_solar_data(self, parameters: dict[str, str]) -> dict:
        # Set up the API endpoint and make a GET request with the provided parameters
        api = SOLAR_API
        logging.info("Fetching solar data from API with provided parameters" )
        response = requests.get(f"{api}", params=parameters)

        # Check if the response was successful (status code 200)
        if response.status_code == 200:
            logging.info("Successfully fetched solar data from API.")
        else:
            logging.info(
                f"There's a {response.status_code} error when fetching solar data from API.")
        return response.json()

# if __name__ == "__main__":
#     api_call = get_solar_data()
