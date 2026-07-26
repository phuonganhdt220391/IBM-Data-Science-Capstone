# spacex_web_scraping.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all wikitable elements
tables = soup.find_all('table', "wikitable plainrowheaders")
print(f"Found {len(tables)} target tables on Wikipedia.")

# Extracting table rows for launch log analysis
launch_data = []
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['td', 'th'])
        cols = [ele.text.strip() for ele in cols]
        if len(cols) > 0:
            launch_data.append(cols[:3]) # Capture initial columns

print(f"Successfully extracted {len(launch_data)} raw rows via web scraping.")