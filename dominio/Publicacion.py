

class Publicacion:
    def __init__(self, publicacion, id_user):
        self.publicacion = publicacion
        self.id_p = None
        self.id = id_user

    def __str__(self):
        return f'{self.publicacion}---{self.id_p}---{self.id}'

    def _guardar_public(self):
        from infraestructura.persistenciapublicacion import PersistenciaPublicacion
        persistencia_publicacion = PersistenciaPublicacion()
        persistencia_publicacion.guardar_p(self)

