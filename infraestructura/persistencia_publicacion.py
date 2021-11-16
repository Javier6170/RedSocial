import sqlite3

class Persistencia_publicacion():
    def connect(self):
        self.con = sqlite3.connect("RedYe!.sqlite")
        print(self.con.cursor())
        self.__crear_tabla()

        def __crear_tabla_publicacion(self):
            try:
                cursor = self.con.cursor()
                query = "CREATE TABLE " \
                        "Publicacion(" \
                        "id_p Integer PRIMARY KEY Autoincrement," \
                        "textoArea text)"
                cursor.execute(query)
            except sqlite3.OperationalError as ex:
                pass

        def guardar(self, publicacion):
            cursor = self.con.cursor()
            query = "insert into Publicacion" \
                    "(textoArea)" \
                    "values(?)"
            cursor.execute(query, (publicacion.textoArea))
            self.con.commit()