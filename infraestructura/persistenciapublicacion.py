import sqlite3


class PersistenciaPublicacion():
    def __init__(self):
        self.connect()

    def connect(self):
        self.con = sqlite3.connect("RedYePublicaciones!.sqlite")
        print(self.con.cursor())
        self.__crear_tabla_publicacion()

    def __crear_tabla_publicacion(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE " \
                    "Publicacion(" \
                    "id_p Integer PRIMARY KEY Autoincrement," \
                    "publicacion Text," \
                    "nombre_usuario Text," \
                    "apellido_usuario Text)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_p(self, publicacion):
        cursor = self.con.cursor()
        query = "insert into Publicacion" \
                "(publicacion," \
                "nombre_usuario," \
                "apellido_usuario)" \
                "values(?,?,?)"
        cursor.execute(query, (publicacion.publicacion,
                               publicacion.nombre_usuario,
                               publicacion.apellido_usuario))
        self.con.commit()

    def cargar_todo_p(self):
        from dominio.Publicacion import Publicacion
        cursor = self.con.cursor()
        publicaciones = cursor.execute("select publicacion,nombre_usuario,apellido_usuario"
                                       " from Publicacion")
        cuentas = []
        for publicacion \
                in publicaciones:
            publicacion_cargada = Publicacion(publicacion)
            cuentas.append(publicacion_cargada)
        return cuentas
