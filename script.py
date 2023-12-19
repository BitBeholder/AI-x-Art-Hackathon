import pygame
import requests
import time
from datetime import datetime, timedelta

# Initialize pygame for audio
pygame.mixer.init()

# Load the drum sound
drum_sound = pygame.mixer.Sound('/Users/ernesti/Desktop/aixart/public/1.mp3')  # Replace with the path to your drum sound file

# Function to fetch the latest BPM from Oura
def get_latest_bpm(access_token):
    # Define the API endpoint and headers
    url = "https://api.ouraring.com/v2/usercollection/heartrate"
    headers = {'Authorization': f'Bearer {access_token}'}

    # Define the start and end times for the data
    start_date = (datetime.now() - timedelta(seconds=5)).isoformat()
    end_date = datetime.now().isoformat()

    # Make the API request
    response = requests.get(url, headers=headers, params={'start_date': start_date, 'end_date': end_date})
    print(f"API Response: {response.status_code}, {response.text}")  # Debugging line
    if response.status_code == 200:
        data = response.json()
        if "data" in data and data["data"]:
            latest_bpm = data["data"][-1].get('bpm', 60)  # Default to 60 BPM if not available
            return latest_bpm
        else:
            print("No data available in response.")
            return 60
    else:
        print(f"Error fetching BPM data: {response.status_code}, {response.text}")
        return 60  # Default BPM if error


# Main function to play drum sound based on BPM
def main():
    access_token = 'HIHJUXCO6RLDMUVDPSFD5IKQWRDEH4FR'  # Replace with your actual token
    while True:
        bpm = get_latest_bpm(access_token)
        interval = 60 / bpm  # Time interval between beats in seconds
        print(f"BPM: {bpm}, playing drum beat every {interval:.2f} seconds.")
        drum_sound.play()
        time.sleep(interval)

if __name__ == "__main__":
    main()
