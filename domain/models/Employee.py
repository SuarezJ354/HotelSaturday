from curses.ascii import isdigit

from domain.models.User import User


class Employee(User):

    def __init__(self, id, name , last_name,phone, email, password, status, rol):
        super().__init__(id, name , last_name,phone, email, password, status)
        self._rol = rol

    ROLES_VALIDOS = [
        "Recepcionista", "Conserje", "Servicio al cliente", "Chef", "Cocinero",
        "Mesero", "Bartender", "Supervisor de limpieza", "Ama de llaves",
        "Técnico de mantenimiento", "Gerente general", "Gerente de operaciones",
        "Recursos humanos", "Contador", "Guardia de seguridad", "Supervisor de seguridad"
    ]

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        while True:
            try:
                if rol not in Employee.ROLES_VALIDOS:
                    raise ValueError(f"❌ Error: El rol '{rol}' no es válido. Seleccione uno de la lista.")
                self._rol = rol
                break
            except ValueError as e:
                print(e)
                rol = input("Ingrese un rol válido: ")

    def __str__(self):
        return f"rol{self._rol}"
