import re

from domain.exceptions.CustomExceptions import InvalidEmailError, InvalidPhoneError, InvalidPasswordError


class User:

    def __init__(self, id, name , last_name,phone, email, password, status):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._phone = phone
        self._email = email
        self._password = password
        self._status = status


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        while True:
            try:
                if not  str(id).isdigit() or int(id) <=0:
                    raise ValueError("ERROR: El ID debe ser un numero entero")
                self._id = int(id)
                break
            except ValueError as e:
                print(e)
                id = input("Ingrese un ID válido: ")

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        while True:
            try:
                name = name.strip()
                if not name.isalpha():
                    raise ValueError("❌ Error: El nombre solo debe contener letras.")
                self._name = name
                break
            except ValueError as e:
                print(e)
                name = input("🔄 Ingrese un nombre válido (solo letras): ")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        while True:
            try:
                last_name = last_name.strip()
                if not last_name.isalpha():
                    raise ValueError("❌ Error: El apellido solo debe contener letras.")
                self._last_name = last_name
                break
            except ValueError as e:
                print(e)
                last_name = input("Ingrese un apellido válido (solo letras): ")


    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        while True:
            try:
                if not phone.isdigit() or len(phone) < 7:
                    raise InvalidPhoneError(phone)
                self._phone = phone
                break
            except InvalidPhoneError as e:
                print(f"Error al asignar el teléfono: {e}")
                phone = input("Ingrese un telefono valido: ")


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        while True:
            try:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    raise InvalidEmailError(email)
                self._email = email
                break
            except InvalidEmailError as e:
                print(f"Error: {e}")
                email = input(" Ingrese un correo válido: ")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        while True:
            try:
                if len(password) < 8:
                    raise InvalidPasswordError(password)
                self._password = password
                break
            except InvalidPasswordError as e:
                print(f"Error {e}")
                password = input("Ingrese una contraseña valida: ")


    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status