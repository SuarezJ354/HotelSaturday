from domain.exceptions.CustomExceptions import InvalidPriceError

class Room:
    def __init__(self, id, room_number, room_type, price, status):
        self._id = id
        self._room_number = room_number
        self._room_type = room_type
        self._price = price
        self._status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
        self._room_number = value

    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, value):
        self._room_type = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):

        while True:
            try:
                price = float(price)
                if price < 0:
                    raise InvalidPriceError(price)
                self._price = price
                break
            except InvalidPriceError as e:
                print(f"Error: {e}")
                value = input("Ingrese un numero valido")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
