



from domain.models.Guest import Guest
from application.GuestService import GuestService
from application.GuestInput import GuestInput
from domain.models.Employee import Employee
from application.EmployeeService import EmployeeService
from application.EmployeeInput import EmployeeInput
from application.RoomInput import RoomInput
from application.RoomService import RoomService
from domain.models.Room import Room
from repository.conexion.Conexion import Conexion



class Menu_App:

    db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_saturday')
    db.connection()

    def __init__(self):
        self.guest = Guest(None, None,None,None,None,None,None,None,None)
        self.guest_service = GuestService()
        self.guest_input = GuestInput()
        self.employee = Employee(None, None, None, None, None, None, None, None)
        self.employee_service = EmployeeService()
        self.employee_input = EmployeeInput()
        self.room = Room (None, None, None, None, None)
        self.room_service = RoomService()
        self.room_input = RoomInput()


    def init_app(self):
        init = (int(input("Presione 1 para inicializar: ")))

        while init != 0:

            option = int(input("1. Login \n2. Registro \n3. Salir \nSeleciona una opción: "))

            if option == 1:
                print("Login")
            elif option == 2:
                print("Registro")
                registro = int(input("1. Empleado\n2. Huésped "))
                if registro == 1:
                    self.employee_input.register(self.employee, self.db)
                elif registro == 2:

                    self.room_input.registerRoom(self.room,self.db)
                    self.guest_input.register(self.guest,self.db)
            elif option ==  3:
                print("Saliendo...")
                break



Menu_App()

