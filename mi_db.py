import sqlite3 as db
from datetime import datetime

fecha = datetime.now()
year = fecha.year
mes = fecha.month
dia = fecha.day
hora = fecha.hour
minutos = fecha.minute
segundos = fecha.second
stamp = f"{dia}/{mes}/{year} {hora}:{minutos}:{segundos}"


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
        self.entrada = None

    def inicio_Db(self):
        """Inicia o comprueba la base de datos my_cronos.db"""
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            solicitud = """
                        CREATE TABLE IF NOT EXISTS trabajadores
                        (id text(9) primary key unique,
                        nombre text(30),
                        password text(8) unique,
                        horas_semanales INTEGER,
                        turno_activo text(50))
                        """
            cursor.execute(solicitud)
            solicitud = """
                        CREATE TABLE IF NOT EXISTS turnos
                        (id INTEGER primary key autoincrement,
                        dni text(9),
                        entrada TIMESTAMP,
                        salida TIMESTAMP)
                        """
            cursor.execute(solicitud)

    def add_Turno_entrar(self):
        stamp_1 = stamp
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            solicitud = "INSERT INTO turnos(dni,entrada) VALUES(?,?)"
            cursor.execute(solicitud, (self.dni, stamp_1))
            solicitud = "SELECT id FROM turnos where entrada = ?"
            cursor.execute(solicitud, (stamp_1,))
            id_tur = cursor.fetchone()
        self.entrada = id_tur[0]
        self.actualizar_Trabajador()

    def add_Turno_salir(self):
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            solicitud = "UPDATE turnos SET salida = ? where id = ?"
            cursor.execute(solicitud, (stamp, self.entrada))
        self.entrada = None
        self.actualizar_Trabajador()

    def check_password(self, password) -> str:
        """Devuelve el trabajador con ese password"""
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            solicitud = "SELECT * FROM trabajadores WHERE password = ?"
            cursor.execute(solicitud, (password,))
            respuesta = cursor.fetchone()
        return respuesta

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
        Muestra a los trabajadores de la DB
        """
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            solicitud = "SELECT * FROM trabajadores WHERE id = ?"
            cursor.execute(solicitud, (self.dni,))
            resultado = cursor.fetchone()
        return resultado

    def mostrar_Todos(self) -> list:
        with db.connect("my_cronos.db") as datos:
            cursor = datos.cursor()
            solicitud = "SELECT * FROM trabajadores"
            cursor.execute(solicitud)
            resultado = cursor.fetchall()
        return resultado

    def actualizar_Trabajador(self):
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            solicitud = "UPDATE trabajadores SET turno_activo = ? where id =?"
            cursor.execute(solicitud, (self.entrada, self.dni))


def eliminar_Trabajador(dni):
    with db.Connection("my_cronos.db") as datos:
        cursor = datos.cursor()
        solicitud = "DELETE FROM trabajadores where id=?"
        cursor.execute(solicitud, (dni,))
    return f"{dni} ha sido borrado"
