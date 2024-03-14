import os
import requests

# Get the API key from an environment variable
api_key = os.environ.get('CAT_API_KEY')

# Define the request headers with the API key
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key
}

# The URL for The Cat API
url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"

# Perform the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the result
    print(response.json())
else:
    print(f"Failed to fetch cat images: {response.status_code}")