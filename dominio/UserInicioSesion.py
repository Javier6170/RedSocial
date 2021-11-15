class UsuarioInicioSesion():
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password

    def __str__(self):
        return f'{self.usuario}---{self.password}'

    def _validar(self):
        from infraestructura.persistencia_usuario import PersistenciaUsuario
        persitencia_usuario = PersistenciaUsuario()
        if persitencia_usuario.validarInicioSesion(self) is None:
            return False
        return True

    def validar(self):
        if not self._validar():
            return False
        else:
            return True