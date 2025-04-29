class InvalidEmailError(Exception):
    """Excepción cuando el formato de correo es inválido."""
    def __init__(self, email):
        super().__init__(f"El correo '{email}' no tiene un formato válido.")

class EmailAlreadyExistsError(Exception):
    """Excepción cuando el correo ya está registrado en la base de datos."""
    def __init__(self, email):
        super().__init__(f"❌ Error: El correo '{email}' ya está registrado. Ingrese otro.")

class InvalidPhoneError(Exception):
    """Excepción cuando el teléfono no es numérico o es demasiado corto."""
    def __init__(self, phone):
        super().__init__(f"El teléfono '{phone}' debe contener solo números y al menos 7 dígitos.")

class InvalidPriceError(Exception):
    """Excepción cuando el precio de una habitación es negativo."""
    def __init__(self, price):
        super().__init__(f"El precio '{price}' debe ser un número valido o positivo")

class InvalidPasswordError(Exception):
    """Excepción para que la contraseña sea almenos de 8 digitos"""
    def __init__(self, password):
        super().__init__(f"La contraseña '{password} debe ser almenos de 8 digitos'")