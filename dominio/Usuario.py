from dominio.Cuenta import Cuenta
from infraestructura.persistencia_usuario import PersistenciaUsuario



class Usuario(Cuenta):
    def __init__(self, nombre, apellido, usuario, password):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.id = None

    def _actualizar(self, id):
        from infraestructura.persistencia_usuario import PersistenciaUsuario
        persitencia_usuario = PersistenciaUsuario()
        persitencia_usuario.actualizar(self, id)

    def _guardar(self, usuario):
        from infraestructura.persistencia_usuario import PersistenciaUsuario
        persitencia_usuario = PersistenciaUsuario()
        persitencia_usuario.guardar(self, usuario)

    def guardar(self):
        if self.id is None:
            self._guardar(self.usuario)
        else:
            self._actualizar(self.id)

    def update(self, dict_params):
        self.nombre = dict_params.get('nombre', self.nombre)
        self.apellido = dict_params.get('apellido', self.apellido)
        self.usuario = dict_params.get('usuario', self.usuario)
        self.password = dict_params.get('password', self.password)

    def _actualizar(self, id):
        persitencia_usuario = PersistenciaUsuario()
        persitencia_usuario.actualizar(self, id)

    def _guardar(self, usuario):
        persitencia_usuario = PersistenciaUsuario()
        persitencia_usuario.guardar(self, usuario)

    def guardar(self):
        if self.id is None:
            self._guardar(self.usuario)
        else:
            self._actualizar(self.id)

    def update(self, dict_params):
        self.nombre = dict_params.get('nombre', self.nombre)
        self.apellido = dict_params.get('apellido', self.apellido)
        self.usuario = dict_params.get('usuario', self.usuario)
        self.password = dict_params.get('password', self.password)
