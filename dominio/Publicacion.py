from dominio.Usuario import Usuario


class Publicacion(Usuario):
    def __init__(self, publicacion, id_user,nombre, apellido, usuario, password):
        self.publicacion = publicacion
        self.id_p = None
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.id = id_user
        super().__init__(nombre, apellido, usuario, password)

    def __str__(self):
        return f'{self.publicacion}---{self.id_p}---'
