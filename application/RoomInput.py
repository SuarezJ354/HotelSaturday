

from application.RoomService import RoomService
from domain.models.Room import Room
from repository.persistence.RoomRepository import RoomRepository


class RoomInput:
    def __init__(self):
        self.room = Room(None,None,None,None,None)
        self.room_repository = RoomRepository()

    def registerRoom(self, room, db):
        id = int(input("Ingrese una ID para la habitación: "))
        self.room.id = id
        room_number = int(input("Ingrese el numero de la habitacion: "))
        self.room.room_number = room_number
        room_type = input("Ingrese el tipo de habitacion: ")
        self.room.room_type =room_type
        price = input("Ingrese el precio de la habitacion: ")
        self.room.price = price
        print("1. Disponible \n2. Ocupada\n3. Mantenimiento")
        status = input("Seleccione el estado: ")
        self.room.status = status
        self.room_repository.create_room_repository(self.room, db)



