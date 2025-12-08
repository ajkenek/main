class Property:

    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):

    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):

        return f'Dom o powierzchni {self.area}, {self.rooms} pokoje, cena {self.price}, adres {self.address}, rozmiar działki {self.plot}'
