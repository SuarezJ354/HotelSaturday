import re
import mysql.connector
from application.EmployeeService import EmployeeService
from domain.models.Employee import Employee
from repository.persistence.EmployeeRepository import EmployeeRepository
from domain.exceptions.CustomExceptions import InvalidEmailError, InvalidPhoneError, InvalidPasswordError


class EmployeeInput:
    def __init__(self):
        self.employee = Employee(None, None, None, None, None, None, None, None)
        self.employee_repository = EmployeeRepository()


    def input_id(self):
        while True:
            id = input("Ingrese su documento de identidad: ").strip()
            if id.isdigit() and 1 <= len(id) <=10:
                return id
            print("❌ ID inválido. Debe ser un número positivo y máximo de 10 dígitos.")

    def input_name(self, prompt):
        while True:
            value = input(prompt).strip()
            if value.isalpha():
                return value
            print("❌ Solo se permiten letras")

    def input_phone(self):
        while True:
            phone = input("Ingrese su telefono: ").strip()
            if phone.isdigit() and len(phone) >= 7:
                return phone
            print("❌ Teléfono inválido. Debe tener al menos 7 dígitos")

    def input_email(self):
        while True:
            email = input("Ingrese su correo: ").strip()
            if re.match(r"[^@]+@[^@]+\.[^@]", email):
                return email
            print("❌ Correo inválido.")

    def input_password(self):
        while True:
            password = input("Ingrese su contraseña (minimo 8 caracteres): ").strip()
            if len(password) >= 8:
                return password
            print("❌ La contraseña debe tener al menos 8 caracteres")
    def input_status(self):
        while True:
            status = input("1. Activo\n2. Inactivo\nSeleccione el estado: ").strip()
            if status in ['1', '2']:
                return int(status)
            print("❌ Opción inválida.")

    def input_role(self):
        roles ={
            '1': "Recepcionista",
            '2': "Conserje",
            '3': "Servicio al cliente"
        }
        while True:
            print("1. Recepcionista\n2. Conserje\n3. Servicio al cliente\n4. Otro")
            rol = input("Seleccione su rol: ").strip()
            if rol in roles:
                return roles[rol]
            elif rol == '4':
                print("Muy pronto tendremos otros puestos disponibles.")
            else:
                print("❌ Opción inválida.")

    def register(self, employee, db):
        self.employee.id = self.input_id()
        self.employee.name = self.input_name("Ingrese su nombre: ")
        self.employee.last_name = self.input_name("Ingrese su apellido: ")
        self.employee.phone = self.input_phone()
        self.employee.email = self.input_email()
        self.employee.password = self.input_password()
        self.employee.status = self.input_status()
        self.employee.rol = self.input_role()

        try:
            self.employee_repository.create_employee_repository(self.employee, db)
            print("✅ Empleado registrado exitosamente.")
        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:
                print(f"❌ ERROR: Ya existe un usuario registrado con ese ID o correo.")
            else:
                print(f"❌ ERROR inesperado: {e}")