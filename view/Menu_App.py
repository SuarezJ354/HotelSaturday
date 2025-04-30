



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
        self.guest = Guest(None, None,None,None,None,None,None,None,None)
        self.guest_service = GuestService(self.db)
        self.guest_input = GuestInput()
        self.employee = Employee(None, None, None, None, None, None, None, None)
        self.employee_service = EmployeeService(self.db)
        self.employee_input = EmployeeInput()
        self.room = Room (None, None, None, None, None)
        self.room_service = RoomService(self.db)
        self.room_input = RoomInput()



    def init_app(self):
        init = (int(input("Presione 1 para inicializar\nPresione 0 para finalizar: ")))
        while init != 0:

            while True:
                try:
                    option = int(input("1. Login \n2. Registro \n3. Salir \nSelecciona una opción: ").strip())
                    match option:
                        case 1:
                            while True:
                                try:
                                    login = int(input("1. Empleado\n2. Huésped\n3. Salir\nSeleccione una opción: ").strip())
                                    if login == 1:
                                        self.employee_service.login(self.db)
                                    elif login == 2:
                                        self.guest_service.login(self.db)
                                    elif login == 3:
                                        print("Saliendo...")
                                        break
                                    else:
                                        print("ERROR: Elija una opción correcta: ")
                                except ValueError:
                                    print("⚠ ERROR: Debes ingresar un número válido")
                        case 2:
                            while True:
                                try:
                                    print("Registro")
                                    registro = int(input("1. Empleado\n2. Huésped\n3. Salir\nSelecciona una opción: "))
                                    if registro == 1:
                                        self.employee_input.register(self.employee, self.db)
                                    elif registro == 2:
                                        self.guest_input.register(self.guest,self.db)
                                    elif registro == 3:
                                        print("Saliendo...")
                                        break
                                    else:
                                        print("⚠ ERROR: Elija una opción correcta")
                                except ValueError:
                                    print("⚠ ERROR: Debes ingresar un número válido")
                        case 3:
                            print("Saliendo...")
                            return
                        case _:
                            print("⚠ ERROR: Elija una opción correcta")
                    break
                except ValueError:
                    print("⚠ ERROR: Debes ingresar un número válido")

