from flask import Flask, request, jsonify, make_response
from model import Model
from ModelConn import ClienteModel
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/v1/aula/consultar/', methods=["GET"])
def consultar():
    return Model.jsonReturn()


@app.route('/v1/aula/consultar/cliente', methods=["GET"])
def consultarCliente():
    return Model.soma()

@app.route('/v1/aula/cadastrar', methods=["GET"])
def cadastrarEmail():
    return ClienteModel.cadastrarEmail()

@app.route('/v1/aula/cadastrar/atualizar', methods=["GET"])
def atualizar():
    return ClienteModel.atualizar()

if __name__ == '__main__':
    app.run(debug=True,port= 5000)