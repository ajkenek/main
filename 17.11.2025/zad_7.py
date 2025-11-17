import requests

class Brewery:
    def __init__(self, name: str, brewery_type: str, city: str, state: str):
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state

    def __str__(self):
        return f"🍺 {self.name} ({self.brewery_type}) - {self.city}, {self.state}"

data = requests.get("https://api.openbrewerydb.org/v1/breweries?per_page=20").json()

lista_browarow = [Brewery(b['name'], b['brewery_type'], b['city'], b['state']) for b in data]

for browar in lista_browarow:
    print(browar)