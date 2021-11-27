class Publicacion:
    def __init__(self,id_p=None,publicacion=None, nombre_usuario=None, apellido_usuario=None):
        self.publicacion = publicacion
        self.id_p = id_p
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

    def _traer_publicaciones(self):
        from infraestructura.persistenciapublicacion import PersistenciaPublicacion
        persistencia_publicacion = PersistenciaPublicacion()
        return persistencia_publicacion.cargar_todo_p()

    def traer_publicaciones(self):
        return self._traer_publicaciones()
