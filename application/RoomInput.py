import mysql.connector
from domain.models.Room import Room
from repository.persistence.RoomRepository import RoomRepository

class RoomInput:
    def __init__(self):
        self.room_repository = RoomRepository()

    def registerRoom(self, room, db):
        print("\n=== Registro de Habitación ===")
        room = Room(None, None, None, None, None)
        while True:
            try:
                room_number = int(input("Ingrese el numero de la habitación: ").strip())
                if room_number <= 0 or room_number > 9999:
                    print("❌ ERROR: El número debe ser positivo y máximo 4 dígitos.")
                    continue
                break
            except ValueError:
                print("❌ ERROR: Debes ingresar un número válido.")
        room.room_number = room_number

        while True:
            room_type = input("Ingrese el tipo de habitación (Ej: Deluxe, Suite): ").strip()
            if not room_type or room_type.isdigit():
                print("❌ ERROR: El tipo de habitación no puede ser vacío ni numérico.")
                continue
            break
        room.room_type = room_type

        while True:
            try:
                price = float(input("Ingrese el precio de la habitación: ").strip())
                if price <= 0:
                    print("❌ ERROR: El precio debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("❌ ERROR: Debes ingresar un número válido.")
        room.price = price

        estados = {1: "Disponible", 2: "Ocupada", 3: "Mantenimiento"}
        while True:
            print("1. Disponible \n2. Ocupada \n3. Mantenimiento")
            try:
                option = int(input("Seleccione el estado de la habitación: ").strip())
                if option not in estados:
                    print("❌ ERROR: Seleccione una opción válida.")
                    continue
                break
            except ValueError:
                print("❌ ERROR: Debe ingresar un número válido.")
        room.status = estados[option]

        try:
            self.room_repository.create_room_repository(room, db)
            print(f"✅ Habitación {room.room_number} registrada exitosamente.")
        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:
                print(f"❌ ERROR: Ya existe una habitación registrada con el número {room.room_number}. No se puede registrar nuevamente.")
            else:
                print(f"❌ ERROR inesperado: {e}")
