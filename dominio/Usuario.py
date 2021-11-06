from dominio.Cuenta import Cuenta

class Usuario(Cuenta):
    def __init__(self, nombre, apellido, usuario, password):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
