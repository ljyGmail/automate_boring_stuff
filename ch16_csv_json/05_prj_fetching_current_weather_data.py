import json
import requests
import sys

APPID = '3c2f7ae11cc7fb2cf1e03805bc7e5376'

# Compute location from command line arguments
if (len(sys.argv)) < 2:
    print('Usage: 05_prj_fetching_current_weather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&cnt=3&appid=%s' % (
    location, APPID)
response = requests.get(url)
response.raise_for_status()

print(response.text)
