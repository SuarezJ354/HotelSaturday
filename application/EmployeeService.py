
from domain.models.Employee import Employee
from application.RoomService import RoomService
from application.GuestService import GuestService
from application.RoomInput import RoomInput
from domain.models.Room import Room

class EmployeeService:

    register_data = []

    def __init__(self, db):
        self.room_input = RoomInput()
        self.db = db
        self.guest_service = GuestService(self.db)
        self.room_service = RoomService(self.db)
        self.room = Room (None, None, None, None, None)
        self.employee = Employee (None, None, None, None, None, None, None, None)

    def createEmployee(self, employee):
        employee.id = self.register_data[0]
        employee.name = self.register_data[1]
        employee.last_name = self.register_data[2]
        employee.phone = self.register_data[3]
        employee.email = self.register_data[4]
        employee.password = self.register_data[5]
        employee.status = self.register_data[6]
        employee.rol = self.register_data[7]

    def print_data(self, db):

        query = "SELECT id, name, status FROM employee WHERE rol = 'Conserje'"
        try:
            result = self.db.execute_query(query)
        except Exception as e:
            print(f"❌ ERROR en consulta SQL: {e}")
            return []
        if not result:
            print("❌ No hay conserjes disponibles.")
            return []

        print("\nConserjes disponibles: ")
        for concierge in result:
            id, name, status = concierge
            print(f"ID: {id} | Nombre: {name} | Estado: {status}")
        return result


    def login(self, db):
        print("=== Inicio de Sesión ===")

        email = input("Ingrese su correo: ").strip()
        password = input("Ingrese su contraseña: ").strip()

        query = "SELECT id, name, password, rol FROM employee WHERE email = %s"
        params = (email,)

        result = db.execute_query(query, params)

        if not result:
            print("❌ Error: Usuario no encontrado.")
            return False
        try:
            user_id, user_name, stored_password, user_rol = result[0]
        except ValueError:
            print("⚠ ERROR: La consulta no devolvió los datos esperados.")
            return False

        if password == stored_password:
            print(f"✅ Bienvenido {user_rol}, {user_name}! Inicio de sesión exitoso.")
            while True:
                match user_rol:
                    case "Conserje":
                        print("1. Ver habitaciones\n2. Limpiar habitación\n3. Salir")
                        try:
                            option = int(input("Selecciona una opción: "))
                            match option:
                                case 1:
                                    self.room_service.print_data_service()
                                case 2:
                                    print("Seleccione una habitación para limpiar")
                                    print("Limpiando...")
                                case 3:
                                    print("Saliendo del menú...")
                                    break
                                case _:
                                    print("⚠ ERROR: Elija una opción correcta")
                        except ValueError:
                            print("⚠ ERROR: Debes ingresar un número válido.")

                    case "Recepcionista":
                        print("1. Ver huéspedes\n2. Ver habitaciones\n3. Registrar habitación\n4. Editar huésped\n5. Salir")
                        try:
                            option = int(input("Selecciona una opción: "))
                            match option:
                                case 1:
                                    self.guest_service.print_data_service(self.db)
                                case 2:
                                    self.room_service.print_data_service()
                                case 3:
                                    self.room_input.registerRoom(self.room, self.db)
                                case 4:
                                    self.guest_service.edit_guest(self.db)
                                case 5:
                                    print("Saliendo del menú...")
                                    break
                                case _:
                                    print("⚠ ERROR: Elija una opción correcta")
                        except ValueError:
                            print("⚠ ERROR: Debes ingresar un número válido.")
                    case "Servicio al cliente":
                        print("1. Llamar al conserje\n2. Responder preguntas del huésped\n3. Salir")
                        try:
                            option = int(input("Selecciona una opción: "))
                            match option:
                                case 1:
                                    self.print_data(self.db)
                                case 2:
                                    print("Muy pronto...")
                                case 3:
                                    print("Saliendo...")
                                    break
                                case _:
                                    print("⚠ ERROR: Elija una opción correcta")
                        except ValueError:
                            print("⚠ ERROR: Debes ingresar un número válido.")
            return True
        else:
            print("❌ Error: Contraseña incorrecta.")
            return False