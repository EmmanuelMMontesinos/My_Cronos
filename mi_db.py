import sqlite3 as db


class Trabajador():
    def __init__(self) -> None:
        """
        Clase de transición para el registro en la DB
        """
        self.inicio_Db()
        self.nombre = ""
        self.dni = ""
        self.password = ""
        self.horas_semanales = 40
        self.historial_trabajo = []

    def inicio_Db(self):
        """Inicia o comprueba la base de datos my_cronos.db"""
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            solicitud = """
                        CREATE TABLE IF NOT EXISTS trabajadores(
                        id text(9) primary key,
                        nombre text(30),
                        password text(8),
                        horas_semanales INTEGER,
                        )
                        """
            cursor.execute(solicitud)

    def add_Trabajador(self) -> None:
        """
        Añade al trabajador en la DB
        """
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            solicitud = "INSERT INTO trabajadores(id,nombre,password,horas_semanales) VALUES(?,?,?,?)"
            cursor.execute(solicitud, (self.dni, self.nombre,
                           self.password, self.horas_semanales))

    def mostrar_Trabajador(self) -> list:
        """
        Añade al trabajador en la DB
        """
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            solicitud = "SELECT * FROM trabajadores WHERE id = ?"
            cursor.execute(solicitud, (self.dni,))
            resultado = cursor.fetchone()
        return resultado
