from domain.models.Guest import Guest
from application.GuestService import GuestService
from application.GuestInput import GuestInput
from domain.models.Employee import Employee
from application.EmployeeService import EmployeeService
from application.EmployeeInput import EmployeeInput
from application.RoomInput import RoomInput
from application.RoomService import RoomService
from domain.models.Room import Room

class Menu_App:
    def __init__(self, db):
        self.db = db
        self.guest_service = GuestService(self.db)
        self.guest_input = GuestInput()
        self.employee_service = EmployeeService(self.db)
        self.employee_input = EmployeeInput()
        self.room_service = RoomService(self.db)
        self.room_input = RoomInput()


    def pedir_opcion(self, mensaje):
        while True:
            try:
                return int(input(mensaje).strip())
            except ValueError:
                print("⚠️ ERROR: Debes ingresar un número válido.")

    def init_app(self):
        while True:
            option = self.pedir_opcion("\n=== Menú Principal ===\n1. Login\n2. Registro\n3. Salir\nSelecciona una opción: ")

            match option:
                case 1:
                    self.menu_login()
                case 2:
                    self.menu_registro()
                case 3:
                    print("👋 Saliendo de la aplicación... ¡Hasta luego!")
                    return
                case _:
                    print("⚠️ Opción no válida")

    def menu_login(self):
        while True:
            login = self.pedir_opcion("\n=== Login ===\n1. Empleado\n2. Huésped\n3. Volver\nSelecciona una opción: ")

            match login:
                case 1:
                    self.employee_service.login(self.db)
                case 2:
                    self.guest_service.login(self.db)
                case 3:
                    return
                case _:
                    print("⚠️ Opción no válida")

    def menu_registro(self):
        while True:
            registro = self.pedir_opcion("\n=== Registro ===\n1. Empleado\n2. Huésped\n3. Volver\nSelecciona una opción: ")

            match registro:
                case 1:
                    self.employee_input.register(None, self.db)
                case 2:
                    self.guest_input.register(None, self.db)
                case 3:
                    return
                case _:
                    print("⚠️ Opción no válida")


