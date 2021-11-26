import sqlite3


class PersistenciaUsuario():

    def __init__(self):
        self.connect()

    def connect(self):
        self.con = sqlite3.connect("RedYe!.sqlite")
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE " \
                    "Usuario(" \
                    "id Integer PRIMARY KEY Autoincrement," \
                    "usuario text," \
                    "nombre text," \
                    "apellido text," \
                    "password text)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar(self, usuario):
        cursor = self.con.cursor()
        query = "insert into Usuario" \
                "(nombre, " \
                "apellido, " \
                "usuario, " \
                "password)" \
                "values(?,?,?,?)"
        cursor.execute(query, (usuario.nombre,
                               usuario.apellido,
                               usuario.usuario,
                               usuario.password))
        self.con.commit()

    def cargar_todo(self):
        from dominio.Usuario import Usuario
        cursor = self.con.cursor()
        usuarios = cursor.execute("select nombre,apellido,usuario,"
                                  "password "
                                  " from Usuario")
        cuentas = []
        for nombre, apellido, usuario, password \
                in usuarios:
            cuenta_cargada = Usuario(nombre, apellido, usuario, password)
            cuentas.append(cuenta_cargada)
        return cuentas

    def cargar(self, id):
        from dominio.Usuario import Usuario
        cursor = self.con.cursor()
        usuarios = cursor.execute(
            "select nombre,apellido,usuario,password"
            " from Usuario where id = ?", (id,))
        cuenta_cargada = None
        for nombre, apellido, usuario, password in usuarios:
            cuenta_cargada = Usuario(nombre, apellido, usuario, password)
        return cuenta_cargada

    def validar(self, usuario):
        from dominio.Usuario import Usuario
        cursor = self.con.cursor()
        usuarios = cursor.execute("SELECT nombre,apellido,usuario,password FROM Usuario "
                                  "WHERE usuario=?", (usuario.usuario,))
        personaExistente = None
        for nombre, apellido, usuario, password in usuarios:
            personaExistente = Usuario(nombre, apellido, usuario, password)
        return personaExistente

    def validarInicioSesion(self, usuarioInicio):
        from dominio.Usuario import Usuario
        cursor = self.con.cursor()
        usuarios = cursor.execute("SELECT nombre,apellido,usuario,password FROM Usuario "
                                  "WHERE usuario=? AND password = ?", (usuarioInicio.usuario, usuarioInicio.password))
        personaExistente = None
        for nombre, apellido, usuario, password in usuarios:
            personaExistente = Usuario(nombre, apellido, usuario, password)
        return personaExistente

    def actualizar(self, usuario, id):
        query = 'update Usuario set nombre=?,apellido=?,usuario=?,password=?,' \
                'where id=?'
        cursor = self.con.cursor()
        cursor.execute(query, (usuario.nombre,
                               usuario.apellido,
                               usuario.usuario,
                               usuario.password,
                               id))
        self.con.commit()
