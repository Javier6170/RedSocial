class Publicacion:
    def __init__(self, publicacion, nombre_usuario, apellido_usuario):
        self.publicacion = publicacion
        self.id_p = None
        self.nombre_usuario= nombre_usuario
        self.apellido_usuario = apellido_usuario

    def __str__(self):
        return f'{self.publicacion}---{self.id_p}---{self.apellido_usuario}---{self.nombre_usuario}'

    def _guardar_public(self):
        from infraestructura.persistenciapublicacion import PersistenciaPublicacion
        persistencia_publicacion = PersistenciaPublicacion()
        persistencia_publicacion.guardar_p(self)

    def guardarPublicacion(self):
        self._guardar_public()
