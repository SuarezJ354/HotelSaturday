
from domain.models.Employee import Employee

class EmployeeService:

    register_data = []

    def __init__(self):
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

    def print_data_service(self):
        for data in self.register_data:
            print(data)