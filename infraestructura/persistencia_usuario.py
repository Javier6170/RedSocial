import sqlite3


class PersistenciaUsuario():

    def __init__(self):
        self.connect()

    def connect(self):
        self.con = sqlite3.connect("RedYe!.sqlite")
        print(self.con.cursor())
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE " \
                    "Usuario(" \
                    "usuario Text UNIQUE," \
                    "nombre Text," \
                    "apellido text," \
                    "password text"
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
                "values(" \
                " ?,?,?,?)"
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
                                  " from usuario")
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

    def actualizar(self, usuario, id):
        print(id)
        query = 'update Usuario set nombre=?,apellido=?,password=?,' \
                'where id=?'
        cursor = self.con.cursor()
        cursor.execute(query, (usuario.nombre,
                               usuario.apellido,
                               usuario.password,
                               id))
        self.con.commit()
