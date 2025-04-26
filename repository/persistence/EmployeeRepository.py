

from domain.models.Employee import Employee

class EmployeeRepository:
    def __init__(self):
        self.employee = Employee

    def create_employee_repository(self, employee, db):
        query = ("INSERT INTO employee (id,name,last_name,phone,email,password,status,rol) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)")
        values = (employee.id, employee.name, employee.last_name, employee.phone, employee.email, employee.password, employee.status, employee.rol)
        db.execute_query(query, values)