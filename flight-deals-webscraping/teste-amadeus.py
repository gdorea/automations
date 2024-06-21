import requests

# Replace with your Amadeus API credentials
client_id = '21ucKrkGl4brdHCCAly6suBFz2IAKARi'
client_secret = 'yntVpJXwn1vVFxSB'

# Get access token
def get_access_token(client_id, client_secret):
    url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('access_token')

# Search for flights
def search_flights(access_token, origin, destination, departure_date, return_date):
    url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    params = {
        'originLocationCode': origin,
        'destinationLocationCode': destination,
        'departureDate': departure_date,
        'returnDate': return_date,
        'adults': 1,
        'nonStop': 'false',
        'max': 5,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Get access token
access_token = get_access_token(client_id, client_secret)

# Search for flights
origin = 'GRU'  # São Paulo
destination = 'GIG'  # Rio de Janeiro
departure_date = '2024-09-20'
return_date = '2024-09-23'
flight_data = search_flights(access_token, origin, destination, departure_date, return_date)

# Print flight details
for flight in flight_data.get('data', []):
    print(f"Flight: {flight}")

