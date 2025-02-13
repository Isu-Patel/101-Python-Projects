import requests

# Define the API endpoint and the query parameters
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Gandhinagar",  # City for which we need the weather information
    "appid": "34f5d54afdf523be2ef76445c66acfdd",  # Your API key
    "units": "metric"  # Units for temperature (Celsius)
}

# Make a GET request to the API endpoint with the specified parameters
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract the temperature from the response data
    temperature = data["main"]["temp"]
    # Print the temperature in a formatted string
    print(f"The temperature in Gandhinagar is {temperature} degrees Celsius.")
else:
    # Print an error message if the request was not successful
    print("Failed to retrieve weather data.")

# ---------------------------- Output ---------------------------- #
# The temperature in Gandhinagar is 25.0 degrees Celsius.
