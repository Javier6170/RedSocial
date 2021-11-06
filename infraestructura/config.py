import sqlite3


class Config():
    instacia = None

    def __init__(self):
        self.usaBase = True

    @classmethod
    def obtener_instancia(cls):
        if cls.instacia is None:
            cls.instacia = cls.__load()
        return cls.instacia

    @classmethod
    def connect(cls):
        cls.con = sqlite3.connect("RedYe!.sqlite")
        cls.__crear_tabla()

    @classmethod
    def __crear_tabla(cls):
        try:
            cursor = cls.con.cursor()
            query = "CREATE TABLE " \
                    "UsaBase(" \
                    "prendido INTEGER) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    @classmethod
    def setUsaBase(cls, usaBase):
        instacia = cls.obtener_instancia()
        instacia.usaBase = usaBase
        cls.__update(instacia)
        cls.instacia = instacia

    @classmethod
    def __update(cls, instacia):
        cursor = cls.con.cursor()
        query = "update UsaBase set prendido = ? "
        cursor.execute(query, (instacia.usaBase,))

        cls.con.commit()

    @classmethod
    def __save(cls, instacia):
        cursor = cls.con.cursor()
        query = "insert into UsaBase (prendido) values (?) "
        cursor.execute(query, (instacia.usaBase,))

        cls.con.commit()

    @classmethod
    def __load(cls):
        cls.connect()
        cursor = cls.con.cursor()
        query = "select prendido from UsaBase limit 1"
        cursor.execute(query)
        rows = cursor.fetchall()
        confi_instace = Config()
        if len(rows) == 0:
            confi_instace = Config()
            cls.__save(confi_instace)

        else:
            confi_instace.usaBase = bool(rows[0][0])
        return confi_instace
