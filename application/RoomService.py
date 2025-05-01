from domain.models.Room import Room

class RoomService:

    def __init__(self, db):
        self.db = db
        self.room = Room (None, None, None,None, None)

    def createRoom(self, room):
        query = ("INSERT INTO room (room_number, room_type, price, status) VALUES (%s, %s, %s, %s)")
        values = (room.room_number, room.room_type, room.price, room.status)
        try:
            self.db.execute_query(query, values)
            print(f"✅ Habitación {room.room_number} registrada exitosamente.")
        except Exception as e:
            print(f"❌ Error al registrar la habitación: {e}")

    def print_data_service(self):
        query = "SELECT id, room_number, room_type FROM room WHERE status = 'Disponible'"
        result = self.db.execute_query(query)

        if not result:
            print("❌ No hay habitaciones disponibles.")
            return []

        print("\n🏨 Habitaciones Disponibles 🏨")
        for habitacion in result:
            id, number, type_ = habitacion
            print(f"ID: {id} | Número: {number} | Tipo: {type_}")
        return result

