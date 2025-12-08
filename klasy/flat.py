class Property:

    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class Flat(Property):

    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):

        return f'Mieszkanie o powierzchni {self.area}, {self.rooms} pokoje, cena {self.price}, adres {self.address}, piętro {self.floor}'
