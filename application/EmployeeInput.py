

from application.EmployeeService import EmployeeService
from domain.models.Employee import Employee
from repository.persistence.EmployeeRepository import EmployeeRepository

class EmployeeInput:
    def __init__(self):
        self.employee = Employee(None, None, None, None, None, None, None, None)
        self.employee_repository = EmployeeRepository()

    def register(self, employee, db):
        id = int(input("Ingrese su documento de identidad: "))
        self.employee.id = id
        name = input("Ingrese su nombre: ")
        self.employee.name = name
        last_name = input("Ingrese su apellido: ")
        self.employee.last_name = last_name
        phone = input("Ingrese su teléfono: ")
        self.employee.phone = phone
        email = input("Ingrese su correo: ")
        self.employee.email = email
        password = input("Ingrese su contraseña: ")
        self.employee.password = password
        print("1. Activo \n2. Inactivo")
        status = input("Seleccione el estado: ")
        self.employee.status = status
        print("1. Recepcionista\n2. Conserje\n3. Encargado de servicio al cliente\n4. Chef\n5. Cocinero\n6. Mesero\n7. Bartender\n8. Supervisor de limpieza\n9. Ama de llaves\n10. Técnico de mantenimiento\n11. Gerente general\n12. Gerente de operaciones\n13. Encargado de recursos humanos\n14. Contador\n15. Guardia de seguridad\n16. Supervisor de seguridad")
        rol = input("Selecione su rol:")
        self.employee.rol = rol
        self.employee_repository.create_employee_repository(self.employee, db)

    def print_data(self):
        self.employee_service.print_data_service()