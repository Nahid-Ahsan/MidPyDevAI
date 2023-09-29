import requests

geocoding_api_url = "https://maps.googleapis.com/maps/api/geocode/json"  # Google Maps geocoding API endpoint


api_key = ""  # api key

def retriever(address):
    # parameters for the API request
    params = {
        "address": address,
        "key": api_key
    }

    response = requests.get(geocoding_api_url, params=params)  # get request to API

    if response.status_code == 200:  # if successful 
        data = response.json()
        if data["status"] == "OK":
            # extract and display latitude and longitude
            location = data["results"][0]["geometry"]["location"]
            lat = location["lat"]
            lng = location["lng"]
            print(f"Address: {address}")
            print(f"Latitude: {lat}")
            print(f"Longitude: {lng}")
        else:
            print("request failed. Status:", data["status"])
    else:
        print("request failed. Status code:", response.status_code)

if __name__ == "__main__":
    address = input("Enter an address: ")
    retriever(address)


"""
Here use Google Maps Geocoding API which is take a address as a input and retrieve the latitude and longitude of this. 

1. API Endpoint and API Key: The API endpoint is the URL where API queries will be made, which Google provides as a constant.
   The API key, which is also defined as a constant, is necessary for authentication when making API queries.

2. retriever function: This function takes an address as input, encapsulates the essential operation of the programme.

3. API Request Parameters: A dictionary called params is defined within the function. It holds the API request parameters.

4. API Request and Response Handling: This includes the previously set API endpoint and parameters.
   If the request was successful (HTTP status code 200), it verifies the HTTP response status code.
   If the call is successful, the code uses'response.json()' to parse the JSON response data. The "status" field in the response data is then checked to ensure it is "OK," indicating successful geocoding.
   If the geocoding is successful, the code retrieves and publishes the latitude and longitude information from the response, along with the input address.



"""