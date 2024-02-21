from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
import modules.mi_db as my_db


server = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(user, password) -> bool:
    """Function to authenticate staff users"""
    request = my_db.Staff()
    request.dni, request.password = user, password
    return request.check_password()


@server.route("/workers/", methods=['GET'])
def send_all_workers() -> jsonify:
    """Send a json with all the workers in the workers table"""
    get_workers = my_db.Worker.show_all(self=my_db.Worker())
    return jsonify(get_workers)


@server.route("/workers/<dni>", methods=['GET'])
def send_one_worker(dni) -> jsonify:
    """Sends a json with a worker from the table workers"""
    worker = my_db.Worker()
    worker.dni = dni
    return jsonify(worker.show_worker())


@server.route("/new_worker/", methods=['POST'])
@auth.login_required
def add_worker() -> str:
    """Add a worker per request in the workers table, Staff users only"""
    new_worker = request.json
    worker = my_db.Worker()
    worker.name, worker.dni, worker.turn_id_entry, worker.hours_week = new_worker[
        "name"], new_worker["dni"], new_worker["turn_id_entry"], new_worker["hours_week"]
    worker.add_worker()
    return f"{worker.name} añadido correctamente"


@server.route("/workers/update/<dni>", methods=["PUT"])
@auth.login_required
def update_worker(dni) -> str:
    """Update a worker in the workers table, only for staff users."""
    updated_worker = request.json
    worker = my_db.Worker()
    worker.dni = dni
    workers_db = worker.show_all()
    if worker.dni in [dni[0] for dni in workers_db]:
        worker.update_worker(updated_worker)
        return f"{updated_worker['name']} ha sido actualizado"
    else:
        return f"{dni} no existe en la Base de Datos"


@server.route("/turns/", methods=["GET"])
@auth.login_required
def show_all_turns() -> jsonify:
    """Displays all shifts of all workers if requested with staff permissions."""
    return jsonify(my_db.show_all_turns_all_workers())


@server.route("/turns/<dni>", methods=["GET"])
@auth.login_required
def show_one_turn(dni):
    """Displays all shifts of a worker by specifying the employee's ID number as long as he/she has staff rights"""
    worker = my_db.Worker()
    worker.dni = dni
    return jsonify(my_db.show_all_turns_one_worker(worker.dni))


@server.route("/delete/<dni>", methods=["DELETE"])
@auth.login_required
def del_worker(dni) -> str:
    """Removes the specified worker as long as you have staff permissions"""
    worker = my_db.Worker()
    worker.dni = dni
    return worker.delete_worker()


server.run(host="0.0.0.0", port=8000)
