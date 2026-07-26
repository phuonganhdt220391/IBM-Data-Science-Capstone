# spacex_api_collection.py
import requests
import pandas as pd

print("Querying SpaceX v4 API for historical launches...")
url = "https://api.spacexdata.com/v4/launches"
response = requests.get(url)
data = response.json()

# Parse basic launch details
launch_list = []
for launch in data:
    launch_dict = {
        "flight_number": launch.get("flight_number"),
        "date": launch.get("date_utc"),
        "rocket": launch.get("rocket"),
        "success": launch.get("success"),
        "launchpad": launch.get("launchpad")
    }
    launch_list.append(launch_dict)

df_api = pd.DataFrame(launch_list)
print(f"Successfully retrieved {len(df_api)} launches from SpaceX API.")
print(df_api.head())