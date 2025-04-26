
from domain.models.Room import Room

class RoomService:

    register_room = []

    def __init__(self):
        self.room = Room (None, None, None,None, None)

    def createRoom(self, room):
        room.id = self.register_room[0]
        room.room_number = self.register_room[1]
        room.room_type = self.register_room[2]
        room.price = self.register_room[3]
        room.status = self.register_room[4]

