
from domain.models.Room import Room
class RoomService:

    register_room = []

    def __init__(self, db):
        self.db = db
        self.room = Room (None, None, None,None, None)

    def createRoom(self, room):
        room.id = self.register_room[0]
        room.room_number = self.register_room[1]
        room.room_type = self.register_room[2]
        room.price = self.register_room[3]
        room.status = self.register_room[4]

    def print_data_service(self):
        query = "SELECT id, room_number, room_type FROM room WHERE status = 'Disponible'"
        result = self.db.execute_query(query)

        if not result:
            print("❌ No hay habitaciones disponibles.")
            return []

        print("\n🏨 **Habitaciones Disponibles** 🏨")
        for habitacion in result:
            id, number, type_ = habitacion
            print(f"ID: {id} | Número: {number} | Tipo: {type_}")
        return result

