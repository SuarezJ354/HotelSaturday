from keyring.backends.libsecret import available

from domain.models.Guest import Guest
from application.RoomService import RoomService

class GuestService:

    def __init__(self, db):
        self.db = db
        self.guest = Guest(None, None, None, None, None, None, None, None, None)
        self.room_service = RoomService(self.db)

    def print_data_service(self, db):

        query = "SELECT id, name, status FROM guest"
        result = self.db.execute_query(query)

        if not result:
            print("❌ No hay huéspedes disponibles.")
            return []

        print("\nHuéspedes")
        for guest in result:
            id, name, status = guest
            print(f"ID: {id} | Nombre: {name} | Estado: {status}")
        return result

    def edit_guest(self, db):
        print("Editando huésped")
        guest_id = input("Ingrese el ID del huésped a modificar").strip()
        if not guest_id.isdigit():
            print("❌ ERROR: El ID debe ser un número.")
            return
        guest_id = int(guest_id)

        query = "SELECT id, name, phone, email, status FROM guest WHERE id = %s"
        params = (guest_id,)
        result = self.db.execute_query(query, params)

        if not result:
            print("No se encontró un huésped con ese ID")
            return

        guest_id, guest_name, guest_phone, guest_email, guest_status = result[0]
        print(f"Editando huésped: {guest_name} (ID: {guest_id}) Estado: {guest_status}")

        print("1. Activo \n2. Inactivo")
        new_status = input("Seleccione el nuevo estado (dejar vacío para mantener):  ").strip() or guest_status
        new_name = input("Nuevo nombre (dejar vacío para mantener): ").strip() or guest_name
        new_phone = input("Nuevo teléfono (dejar vacío para mantener): ").strip() or guest_phone

        update_query = "UPDATE guest SET status = %s, name = %s, phone = %s WHERE id = %s"
        update_params = (new_status, new_name, new_phone, guest_id)
        self.db.execute_query(update_query, update_params)

        print("✅ Huésped actualizado.")
    def hospedarse(self, guest_id):
        print("\n=== Hospedarse en una habitación ===")

        query = "SELECT room_id FROM guest WHERE id = %s"
        params = (guest_id,)
        result = self.db.execute_query(query, params)

        if result and result[0][0] is not None:
            current_room_id = result[0][0]
            print(
                f"⚠️ Ya estás hospedado en la habitación ID: {current_room_id}. No puedes hospedarte en otra habitación.")
            return

        available_rooms = self.room_service.print_data_service()
        if not available_rooms:
            print("⚠ No hay habitaciones disponibles.")
            return

        room_id = input("Ingrese el ID de la habitacion que desea hospedarse: ").strip()
        if not room_id.isdigit():
            print("❌ ERROR: Debe ingresar un número de ID válido.")
            return
        room_id = int(room_id)

        query = "SELECT id, status FROM room WHERE id =%s"
        params = (room_id,)
        result = self.db.execute_query(query, params)

        if not result:
            print("❌ No existe una habitacion con ese ID")
            return
        _, status = result[0]
        if status != "Disponible":
            print("❌ La habitacion no esta disponible.")
            return


        update_room_query = "UPDATE room SET status = 'Ocupada' WHERE id = %s"
        self.db.execute_query(update_room_query, (room_id,))

        assign_guest_query = "UPDATE guest SET room_id = %s WHERE id = %s"
        self.db.execute_query(assign_guest_query, (room_id, guest_id))

        print(f"✅ Hospedaje exitoso en la habitación ID: {room_id}")

    def irse_hotel(self, guest_id):
        print("\n=== Check-out (irse de hotel) ===")
        query = "SELECT room_id FROM guest WHERE id =%s"
        params = (guest_id,)
        result = self.db.execute_query(query, params)

        if not result or result[0][0] is None:
            print("⚠️ No tienes ninguna habitación asignada.")
            return
        room_id = result[0][0]

        update_room_query = "UPDATE room SET status = 'Disponible' WHERE id = %s"
        self.db.execute_query(update_room_query, (room_id,))

        clear_guest_query = "UPDATE guest SET room_id = NULL WHERE id = %s"
        self.db.execute_query(clear_guest_query, (guest_id,))

        clear_guest_status = "UPDATE guest SET status = 'inactive' WHERE id = %s "
        self.db.execute_query(clear_guest_status, (guest_id,))


        print(f"✅ Has dejado la habitación ID: {room_id}. ¡Gracias por tu estadía!")

    def solicitar_servicio(self, guest_id):
        print("\n=== Solicitar servicio de limpieza ===")

        query = "SELECT room_id FROM guest WHERE id = %s"
        params = (guest_id,)
        result = self.db.execute_query(query, params)

        if not result or result[0][0] is None:
            print("⚠️ No puedes solicitar servicio sin estar hospedado.")
            return

        room_id = result[0][0]
        print(f"🧹 Servicio de limpieza solicitado para la habitación ID: {room_id}")

    def login(self, db):
        print("=== Inicio de Sesión ===")
        email = input("Ingrese su correo: ").strip()
        password = input("Ingrese su contraseña: ").strip()

        query = "SELECT id, name, password FROM guest WHERE email = %s"
        params = (email,)
        result = db.execute_query(query, params)

        if not result:
            print("❌ Error: Usuario no encontrado.")
            return False
        try:
            user_id, user_name, stored_password = result[0]
        except ValueError:
            print("⚠ ERROR: La consulta no devolvió los datos esperados.")
            return False

        if password == stored_password:
            print(f"✅ Bienvenido, {user_name}! Inicio de sesión exitoso.")
            while True:
                print("\n--- Menú ---")
                print("1. Ver habitaciones disponibles")
                print("2. Hospedarse en una habitación")
                print("3. Irse del hotel")
                print("4. Prestar servicio")
                print("5. Cerrar sesión")

                try:
                    option = int(input("Selecciona una opción: "))
                    match option:
                        case 1:
                            self.room_service.print_data_service()
                        case 2:
                            self.hospedarse(user_id)
                        case 3:
                            self.irse_hotel(user_id)
                            return
                        case 4:
                            self.solicitar_servicio(user_id)
                        case 5:
                            print("👋 Cerrando sesión...")
                            return
                        case _:
                            print("⚠️ Opción no válida.")
                except ValueError:
                    print("⚠️ ERROR: Debes ingresar un número válido.")
            return True
        else:
            print("❌ Error: Contraseña incorrecta.")
            return False



