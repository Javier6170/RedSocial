class UsuarioTemporal():
    def __init__(self, nombre_usuario, apellido_usuario):
        self.nombre_usuario = nombre_usuario
        self.apellido_usuario = apellido_usuario

    def __str__(self):
        return f'{self.nombre_usuario}---{self.apellido_usuario}'
