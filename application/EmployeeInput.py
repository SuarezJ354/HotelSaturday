

from application.EmployeeService import EmployeeService
from domain.models.Employee import Employee
from repository.persistence.EmployeeRepository import EmployeeRepository

class EmployeeInput:
    def __init__(self):
        self.employee = Employee(None, None, None, None, None, None, None, None)
        self.employee_repository = EmployeeRepository()

    def register(self, employee, db):
        id = input("Ingrese su documento de identidad: ").strip()
        self.employee.id = id
        name = input("Ingrese su nombre: ").strip()
        self.employee.name = name
        last_name = input("Ingrese su apellido: ").strip()
        self.employee.last_name = last_name
        phone = input("Ingrese su teléfono: ").strip()
        self.employee.phone = phone
        email = input("Ingrese su correo: ").strip()
        self.employee.email = email
        password = input("Ingrese su contraseña: ").strip()
        self.employee.password = password
        print("1. Activo \n2. Inactivo")
        status = input("Seleccione el estado: ").strip()
        self.employee.status = status
        print("1. Recepcionista\n2. Conserje\n3. Servicio al cliente\n4. Otro")
        while True:
            try:
                rol = int(input("Seleccione su rol: "))

                if rol == 1:
                    role = "Recepcionista"
                elif rol == 2:
                    role = "Conserje"
                elif rol == 3:
                    role = "Servicio al cliente"
                elif rol == 4:
                    print("Muy pronto tendremos otros puestos")
                    puestosDisponibles =[
                        "Chef", "Cocinero", "Mesero", "Bartender", "Supervisor de limpieza", "Ama de llaves",
                        "Técnico de mantenimiento", "Gerente general", "Gerente de operaciones",
                        "Recursos humanos", "Contador", "Guardia de seguridad", "Supervisor de seguridad"
                    ]
                    continue
                else:
                    print("Opción inválida. Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("❌ Entrada inválida. Debe ingresar un número.")

        self.employee.rol = role
        self.employee_repository.create_employee_repository(self.employee, db)

    def print_data(self):
        self.employee_service.print_data_service()