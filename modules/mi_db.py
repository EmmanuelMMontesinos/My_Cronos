import sqlite3 as db
from datetime import datetime

# clase que gestiona el registro el la DB


class Worker():
    def __init__(self) -> None:
        """
        Transition class for registration in the DB
        """
        self.init_Db()
        self.name = ""
        self.dni = ""
        self.password = ""
        self.hours_semanales = 40
        self.history_turns = []
        self.entrada = None

    def init_Db(self):
        """Start or check the database my_cronos.db"""
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = """
                        CREATE TABLE IF NOT EXISTS trabajadores
                        (id text(9) primary key unique,
                        nombre text(30),
                        password text(8) unique,
                        hours_semanales INTEGER,
                        turno_activo text(50))
                        """
            cursor.execute(request)
            request = """
                        CREATE TABLE IF NOT EXISTS turnos
                        (id INTEGER primary key autoincrement,
                        dni text(9),
                        entrada text,
                        salida text)
                        """
            cursor.execute(request)

    def add_turn_entry(self):
        """Makes an entry in the Entry db on shift"""
        date = datetime.now()
        year = date.year
        mes = date.month
        day = date.day
        hour = date.hour
        minute = date.minute
        second = date.second
        stamp = f"{day}/{mes}/{year} {hour}:{minute}:{second}"
        stamp_1 = stamp
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "INSERT INTO turnos(dni,entrada) VALUES(?,?)"
            cursor.execute(request, (self.dni, stamp_1))
            request = "SELECT id FROM turnos where entrada = ?"
            cursor.execute(request, (stamp_1,))
            id_tur = cursor.fetchone()
        self.entry = id_tur[0]
        self.update_worker()

    def add_turn_out(self):
        """Makes an entry in the out of turn db."""
        date = datetime.now()
        year = date.year
        mes = date.month
        day = date.day
        hour = date.hour
        minute = date.minute
        second = date.second
        stamp_1 = f"{day}/{mes}/{year} {hour}:{minute}:{second}"
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "UPDATE turnos SET salida = ? where id = ?"
            cursor.execute(request, (stamp_1, self.entrada))
        self.entry = None
        self.update_worker()

    def check_password(self, password) -> str:
        """Returns the worker with that password"""
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "SELECT * FROM trabajadores WHERE password = ?"
            cursor.execute(request, (password,))
            response = cursor.fetchone()
        return response

    def add_worker(self) -> None:
        """
        Add the worker in the DB
        """
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "INSERT INTO trabajadores(id,nombre,password,hours_semanales) VALUES(?,?,?,?)"
            cursor.execute(request, (self.dni, self.name,
                           self.password, self.hours_semanales))

    def show_worker(self) -> list:
        """
        Shows DB workers
        """
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "SELECT * FROM trabajadores WHERE id = ?"
            cursor.execute(request, (self.dni,))
            response = cursor.fetchone()
        return response

    def show_all(self) -> list:
        """Displays a list of ALL Workers"""
        with db.connect("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "SELECT * FROM trabajadores"
            cursor.execute(request)
            response = cursor.fetchall()
        return response
# Por implementar

    def update_worker(self):
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "UPDATE trabajadores SET turno_activo = ? where id =?"
            cursor.execute(request, (self.entry, self.dni))


def delete_worker(dni):
    """DELETE a Worker entry"""
    with db.Connection("my_cronos.db") as datos:
        cursor = datos.cursor()
        request = "DELETE FROM trabajadores where id=?"
        cursor.execute(request, (dni,))
    return f"{dni} ha sido borrado"


def show_all_turns_all_workers():
    """Displays ALL the turmos of ALL Workers"""
    with db.Connection("my_cronos.db") as datos:
        cursor = datos.cursor()
        request = "SELECT * FROM turnos"
        cursor.execute(request)
        response = cursor.fetchall()
    return response


def show_all_turns_one_worker(dni):
    """Displays ALL shifts of ONE Worker"""
    with db.Connection("my_cronos.db") as datos:
        cursor = datos.cursor()
        request = "SELECT * FROM turnos where dni = ?"
        cursor.execute(request, (dni,))
        response = cursor.fetchall()
    return response
