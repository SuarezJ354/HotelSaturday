import mysql.connector

from application.GuestService import GuestService
from domain.models.Guest import  Guest
from repository.persistence.GuestRepository import GuestRepository

class GuestInput:


    def __init__(self):
        self.guest = Guest(None,None,None,None ,None,None, None,None,None )
        self.guest_repository = GuestRepository()


    def register(self, guest , db):
        while True:
            try:
                id = input("Ingrese su documento de identidad: ").strip()
                if not id.isdigit() or int(id) <= 0 or len(id) > 10:
                    raise ValueError("❌ ERROR: El ID debe ser un número positivo y máximo 10 dígitos.")
                self.guest.id = id
                break
            except ValueError as e:
                print(e)
        name = input("Ingrese su nombre: ").strip()
        self.guest.name = name
        last_name = input("Ingrese su apellido: ").strip()
        self.guest.last_name = last_name
        phone = input("Ingrese su teléfono: ").strip()
        self.guest.phone = phone
        email = input("Ingrese su correo: ").strip()
        self.guest.email = email
        password = input("Ingrese su contraseña: ").strip()
        self.guest.password = password
        while True:
            try:
                print("1. Activo \n2. Inactivo")
                status = int(input("Seleccione el estado: ").strip())
                if status not in [1, 2]:
                    print("❌ ERROR: Ingrese una de las opciones mostradas.")
                    continue
                break

            except ValueError:
                print("❌ ERROR: Ingrese un número válido.")
        self.guest.status = status

        print("Seleccione su ciudad de origen:")
        print("1. Medellín\n2. Envigado \n3. Sabaneta\n3. Bello\n4. Itaguí\n5. Rionegro")
        print("6. Bogotá\n7. Barranquilla\n8. Cartagena\n9. Otro")
        while True:
            try:
                opcion = int(input("Seleccione su ciudad de origen: "))
                if 1 <= opcion <=8:
                    origenes_validos = [
                        "Medellín", "Envigado", "Sabaneta", "Bello", "Itaguí",
                        "Rionegro", "Bogotá", "Barranquilla", "Cartagena", "Montería"
                    ]
                    origin = origenes_validos[opcion - 1]
                    break
                elif opcion == 9:
                    while True:
                        origin = input("Ingrese su ciudad de origen: ").strip()
                        if not origin or origin.isdigit():
                            print("ERROR: No se puede ingresar un numero como ciudad de origen")
                            continue
                        break
                    break
                else:
                    print("Opción invalida, intenta de nuevo.")
            except ValueError:
                print("Debe ingresar un número válido ")

        self.guest.origin = origin

        while True:
            try:
                occupation = input("Ingrese su ocupación: ").strip()
                if not occupation or occupation.isdigit():
                    print("Ocupación invalida. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Debe ingresar una ocupación valida")
        self.guest.occupation = occupation
        try:
            self.guest_repository.create_guest_repository(self.guest, db)
            print("✅ Huésped registrado exitosamente.")
        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:
                print(f"❌ ERROR: Ya existe un usuario registrado con ese ID o Correo. No se puede registrar nuevamente.")
            else:
                print(f"❌ ERROR inesperado: {e}")