from flask import Flask, jsonify, request

from machine import Machine

app = Flask(__name__)
machine = Machine()

@app.route("/")
def hello_world():
    return "Bienvenue sur l'application de gestion"

@app.route('/machines', methods=["GET"])
def liste_machine():
    return jsonify({"machines": machine.liste() })

@app.route('/machines/<name>', methods=["GET","PUT","DELETE"])
def get_machine(name):
    if request.method == 'GET':
        return jsonify({"machine":machine.get(name)})
    if request.method == 'PUT':
        data = request.form # a multidict containing POST data
        return jsonify({"machine":machine.edit(name,data)})
    if request.method == 'DELETE':
        return jsonify({"machine":machine.delete(name)})
    else:
        return jsonify({"error": 'La méthode utilisée n\'est pas valide'})
