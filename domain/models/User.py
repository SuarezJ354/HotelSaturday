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
        self._id = id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

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
                password = input("Ingrese una contraseña valida")


    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status