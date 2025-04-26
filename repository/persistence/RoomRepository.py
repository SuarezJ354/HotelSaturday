from domain.models.Room import Room

class RoomRepository:

    def create_room_repository(self, room, db):
        query = ("INSERT INTO room (id, room_number, room_type, price, status) VALUES (%s,%s,%s,%s,%s)")
        values = (room.id, room.room_number, room.room_type, room.price, room.status)
        db.execute_query(query, values)