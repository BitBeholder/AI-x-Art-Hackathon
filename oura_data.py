import requests
from datetime import datetime, timedelta

def fetch_oura_data(access_token, start_date, end_date):
    # Get the current time and format it for the API call
    current_time = datetime.utcnow()
    formatted_current_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Calculate the start time (5 minutes ago, as an example)
    start_time = current_time - timedelta(minutes=5)
    formatted_start_time = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Oura API endpoint for daily activity (adjust as needed)
    url = "https://api.ouraring.com/v2/usercollection/heartrate"

    # Headers with the authorization token
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Parameters for the request (dates in 'YYYY-MM-DD' format)
    params = {
        'start_date': formatted_start_time,
        'end_date': formatted_current_time
    }

    # Making the GET request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response
        return response.json()
    else:
        # Handle errors (you can expand this part based on your needs)
        print(f"Error {response.status_code}: {response.text}")
        return None

# Example usage
access_token = 'HIHJUXCO6RLDMUVDPSFD5IKQWRDEH4FR'  # Replace with your actual token
start_date = (datetime.now() - timedelta(seconds=5)).isoformat()  # Replace with your desired start date
end_date = datetime.now().isoformat()    # Replace with your desired end date

data = fetch_oura_data(access_token, start_date, end_date)["data"]

print(data)
