import requests
import time
import folium
from colorama import Fore,init
import os


init(autoreset=True)


def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")


    
    if response.status_code == 200:
        data = response.json()
        position = data['iss_position']
        latitude = position['latitude']
        longitude = position['longitude']
        timestamp = data['timestamp']
        print("")
        print("")
        print(f"Timestamp: {time.ctime(timestamp)}")
        print(f"{Fore.YELLOW}Current ISS Location -> {Fore.BLUE}+Latitude: {Fore.RED}{latitude}, {Fore.BLUE}+Longitude: {Fore.RED}{longitude}")
   
        location = [longitude, latitude]  # Latitude and Longitude of San Francisco



        map = folium.Map(location=location, zoom_start=12)

        # Add a marker
        folium.Marker(
            location,
            popup="current iss location",
            icon=folium.Icon(icon="info-sign")
        ).add_to(map)

        path="D:\YashSharma\Python\Maps\map.html"

        # Save the map to an HTML file
        map.save(path)
        os.startfile(path)
        
    else:
        print(f"Error: Unable to fetch data, status code: {response.status_code}")

if __name__ == "__main__":
    while True:
        get_iss_location()
        break
        