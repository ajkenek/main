import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--city", help="city name")
args = parser.parse_args()


class Brewery:
    def __init__(self, name: str, brewery_type: str, city: str, state: str):
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state

    def __str__(self):
        return f"🍺 {self.name} ({self.brewery_type}) - {self.city}, {self.state}"

url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

if args.city:
    url += f"&by_city={args.city}"

data = requests.get(url).json()

for item in data:
    b = Brewery(item.get('name'), item.get('brewery_type'), item.get('city'), item.get('state'))
    print(b)

