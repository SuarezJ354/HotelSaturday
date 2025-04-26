

from application.RoomService import RoomService
from domain.models.Room import Room
from repository.persistence.RoomRepository import RoomRepository


class RoomInput:
    def __init__(self):
        self.room = Room(None,None,None,None,None)
        self.room_repository = RoomRepository()
        self.room_service = RoomService()

    def registerRoom(self, room, db):
        id = int(input("Ingrese una ID para la habitacion: "))
        self.room.id = id
        room_number = int(input("Ingrese el numero de la habitacion: "))
        self.room.room_number = room_number
        room_type = input("Ingrese el tipo de habitacion: ")
        self.room.room_type =room_type
        price = input("Ingrese el precio de la habitacion: ")
        self.room.price = price
        print("1. Activo \n2. Inactivo")
        status = input("Seleccione el estado: ")
        self.room.status = status
        self.room_repository.create_room_repository(self.room, db)

    def print_data(self):
        self.room_service.print_data_service()