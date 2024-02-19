from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
import modules.mi_db as my_db


server = Flask(__name__)
auth = HTTPBasicAuth()

staff_users = {}


@server.route("/workers/", methods=['GET'])
def send_all_workers() -> jsonify:
    get_workers = my_db.Worker.show_all(self=my_db.Worker())
    return jsonify(get_workers)


@server.route("/workers/<dni>")
def send_one_worker(dni) -> jsonify:
    worker = my_db.Worker()
    worker.dni = dni
    return jsonify(worker.show_worker())


server.run(host="0.0.0.0")
