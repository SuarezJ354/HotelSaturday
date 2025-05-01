import re
import mysql.connector
from application.GuestService import GuestService
from domain.models.Guest import  Guest
from repository.persistence.GuestRepository import GuestRepository

class GuestInput:
    def __init__(self):
        self.guest = Guest(None,None,None,None ,None,None, None,None,None )
        self.guest_repository = GuestRepository()

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

    def _input_text(self, mensaje, campo="valor"):
        while True:
            texto = input(mensaje).strip()
            if texto.isalpha():
                return texto
            print(f"❌ ERROR: {campo.capitalize()} solo debe contener letras.")

    def input_origin(self):
        ciudades = {
            '1': "Medellín",
            '2': "Envigado",
            '3': "Sabaneta",
            '4': "Bello",
            '5': "Itaguí",
            '6': "Rionegro",
            '7': "Bogota",
            '8': "Barranquilla",
            '9': "Cartagena"
        }
        for k, v in ciudades.items():
            print(f"{k}. {v}")
        print("10. Otro")
        while True:
            try:
                opcion = int(input("Seleccione su ciudad de origen: "))
                if  str(opcion) in ciudades:
                    return ciudades[str(opcion)]
                elif opcion == 10:
                    return self._input_text("Ingrese su ciudad de origen: ", "ciudad")
                else:
                    print("❌ Opción inválida, intenta de nuevo.")
            except ValueError:
                print("❌ Debe ingresar un número válido.")

    def register(self, guest , db):
        self.guest.id = self.input_id()
        self.guest.name = self.input_name("Ingrese su nombre: ")
        self.guest.last_name = self.input_name("Ingrese su apellido: ")
        self.guest.phone = self.input_phone()
        self.guest.email = self.input_email()
        self.guest.password = self.input_password()
        self.guest.status = self.input_status()
        self.guest.origin = self.input_origin()
        self.guest.occupation = self._input_text("Ingrese su ocupación: ", "Ocupación")

        try:
            self.guest_repository.create_guest_repository(self.guest, db)
            print("✅ Huésped registrado exitosamente.")
        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:
                print(f"❌ ERROR: Ya existe un usuario registrado con ese ID o correo.")
            else:
                print(f"❌ ERROR inesperado: {e}")