import requests
import json

# Set your API key
api_key = "XXXXXX"

# NOAA API URL for ONI data
base_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"
dataset_id = "ONI"  # This might need to be adjusted based on actual available dataset IDs for ONI
start_date = "1950-01-01"
end_date = "2021-12-31"

# Prepare the request headers
headers = {
    'token': api_key
}

# Prepare the query parameters
params = {
    'datasetid': dataset_id,
    'startdate': start_date,
    'enddate': end_date,
    'limit': 1000  # Adjust limit based on how much data you expect to retrieve
}

# Make the request
response = requests.get(url=base_url, headers=headers, params=params)

# Check the status of the response
if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
else:
    print(f"Failed to fetch data: Status code {response.status_code}")
