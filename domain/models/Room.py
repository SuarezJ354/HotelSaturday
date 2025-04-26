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

    @property
    def room_number(self):
        return self._room_number

    @property
    def room_type(self):
        return self._room_type

    @property
    def price(self):
        return self._price

    @property
    def status(self):
        return self._status