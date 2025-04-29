

from domain.models.Guest import Guest




class GuestService:

    register_data = []

    def __init__(self, db):
        self.db = db
        self.guest = Guest(None, None, None, None, None, None, None, None, None)


    def createGuest(self, guest):
        guest.id = self.register_data[0]
        guest.name = self.register_data[1]
        guest.last_name = self.register_data[2]
        guest.phone = self.register_data[3]
        guest.email = self.register_data[4]
        guest.password = self.register_data[5]
        guest.status = self.register_data[6]

    def print_data_service(self):

        for data in self.register_data:
            print(data)


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

        user_id, user_name, stored_password = result[0]
        if password == stored_password:
            print(f"✅ Bienvenido, {user_name}! Inicio de sesión exitoso.")
            return True
        else:
            print("❌ Error: Contraseña incorrecta.")
            return False

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
        id = input("Ingrese el ID del huésped a modificar").strip()

        query = "SELECT id, name, phone, email, status FROM guest WHERE id = %s"
        params = (id,)
        result = db.execute_query(query, params)

        if not result:
            print("No se encontró un huésped con ese ID")
            return
        guest_id, guest_name, guest_phone, guest_email, guest_status = result[0]

        print(f"Editando huésped: {guest_name} (ID: {guest_id}) Estado: {guest_status}")

        print("1. Activo \n2. Inactivo")
        new_status = input("Seleccione el nuevo estado (dejar vacío para mantener):  ").strip() or guest_status
        new_name = input("Nuevo nombre (dejar vacío para mantener): ").strip() or guest_name
        new_phone = input("Nuevo teléfono (dejar vacío para mantener): ").strip() or guest_phone

        udapte_query = "UPDATE guest SET status = %s, name = %s, phone = %s WHERE id = %s"
        udapte_params = (new_status, new_name, new_phone, guest_id)
        db.execute_query(udapte_query, udapte_params)

        print("Huésped actualizado.")





