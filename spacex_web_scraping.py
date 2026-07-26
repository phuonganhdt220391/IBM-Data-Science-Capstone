import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

url = "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("Successfully fetched SpaceX launch records from Wikipedia.")
# Trích xuất bảng dữ liệu phóng từ Wikipedia
tables = soup.find_all('table', "wikitable plainrowheaders")
print(f"Found {len(tables)} tables on the page.")