from dominio.Cuenta import Cuenta
from infraestructura.persistencia_usuario import PersistenciaUsuario


class Usuario(Cuenta):
    def __init__(self, nombre, apellido, usuario, password):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.id = None

    def __str__(self):
        return f'{self.nombre}---{self.apellido}---{self.usuario}---{self.password}'

    def _actualizar(self, id):
        from infraestructura.persistencia_usuario import PersistenciaUsuario
        persitencia_usuario = PersistenciaUsuario()
        persitencia_usuario.actualizar(id)

    def _guardar(self):
        from infraestructura.persistencia_usuario import PersistenciaUsuario
        persitencia_usuario = PersistenciaUsuario()
        if persitencia_usuario.validar(self) is None:
            persitencia_usuario.guardar(self)
            return "Ok"
        return None

    def _validar(self, usuario, password):
        from infraestructura.persistencia_usuario import PersistenciaUsuario
        persitencia_usuario = PersistenciaUsuario()
        if persitencia_usuario.validarInicioSesion(self, usuario, password) is None:
            return False
        return False

    def guardar(self):
        if self.id is None:
            if self._guardar() is None:
                return None
            return "Ok"
        else:
            self._actualizar(id)

    def validar(self, usuario, password):
        if not self._validar(usuario, password):
            return False
        else:
            return True

    def update(self, dict_params):
        self.nombre = dict_params.get('nombre', self.nombre)
        self.apellido = dict_params.get('apellido', self.apellido)
        self.usuario = dict_params.get('usuario', self.usuario)
        self.password = dict_params.get('password', self.password)
