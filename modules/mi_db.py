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
        self.turn_id_entry = ""
        self.hours_week = 40
        self.history_turns = []
        self.entry = None

    def init_Db(self):
        """Start or check the database my_cronos.db"""
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = """
                        CREATE TABLE IF NOT EXISTS workers
                        (id text(9) primary key unique,
                        name text(30),
                        turn_id_entry text(8) unique,
                        hours_week INTEGER,
                        turn_activate text(50))
                        """
            cursor.execute(request)
            request = """
                        CREATE TABLE IF NOT EXISTS turns
                        (id INTEGER primary key autoincrement,
                        dni text(9),
                        entry text,
                        out text)
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
            request = "INSERT INTO turns(dni,entry) VALUES(?,?)"
            cursor.execute(request, (self.dni, stamp_1))
            request = "SELECT id FROM turns where entry = ?"
            cursor.execute(request, (stamp_1,))
            id_tur = cursor.fetchone()
        self.entry = id_tur[0]
        self.update_worker_turn()

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
            request = "UPDATE turns SET out = ? where id = ?"
            cursor.execute(request, (stamp_1, self.entry))
        self.entry = None
        self.update_worker_turn()

    def check_id_turn(self, id_turn) -> str:
        """Returns the worker with that turn_id_entry"""
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "SELECT * FROM workers WHERE turn_id_entry = ?"
            cursor.execute(request, (id_turn,))
            response = cursor.fetchone()
        return response

    def add_worker(self) -> None:
        """
        Add the worker in the DB
        """
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "INSERT INTO workers(id,name,turn_id_entry,hours_week) VALUES(?,?,?,?)"
            cursor.execute(request, (self.dni, self.name,
                           self.turn_id_entry, self.hours_week))

    def show_worker(self) -> list:
        """
        Shows DB workers
        """
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "SELECT * FROM workers WHERE id = ?"
            cursor.execute(request, (self.dni,))
            response = cursor.fetchone()
        return response

    def show_all(self) -> list:
        """Displays a list of ALL Workers"""
        with db.connect("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "SELECT * FROM workers"
            cursor.execute(request)
            response = cursor.fetchall()
        return response

    def update_worker_turn(self) -> None:
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = "UPDATE workers SET turn_activate = ? where id =?"
            cursor.execute(request, (self.entry, self.dni))

    def update_worker(self, update) -> None:
        with db.Connection("my_cronos.db") as datos:
            cursor = datos.cursor()
            request = """UPDATE workers SET
                        id = ?,
                        name = ?,
                        turn_id_entry = ?,
                        hours_week = ? where id = ?
                        """
            cursor.execute(request, (update["dni"], update["name"],
                           update["turn_id_entry"], update["hours_week"], self.dni))


def delete_worker(dni):
    """DELETE a Worker entry"""
    with db.Connection("my_cronos.db") as datos:
        cursor = datos.cursor()
        request = "DELETE FROM workers where id=?"
        cursor.execute(request, (dni,))
    return f"{dni} ha sido borrado"


def show_all_turns_all_workers():
    """Displays ALL the turmos of ALL Workers"""
    with db.Connection("my_cronos.db") as datos:
        cursor = datos.cursor()
        request = "SELECT * FROM turns"
        cursor.execute(request)
        response = cursor.fetchall()
    return response


def show_all_turns_one_worker(dni):
    """Displays ALL shifts of ONE Worker"""
    with db.Connection("my_cronos.db") as datos:
        cursor = datos.cursor()
        request = "SELECT * FROM turns where dni = ?"
        cursor.execute(request, (dni,))
        response = cursor.fetchall()
    return response
