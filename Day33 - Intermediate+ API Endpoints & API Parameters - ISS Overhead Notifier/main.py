import requests

ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"

def get_response_from(endpoint):
    response = requests.get(url=endpoint)
    response.raise_for_status()
    response = response.json()

    return response

print(get_response_from(ISS_ENDPOINT))
