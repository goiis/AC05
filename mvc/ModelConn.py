from flask import Flask, request, jsonify, make_response
import json
from flask_mysqldb import MySQL
from controler import app



class ClienteModel():

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'bancodeteste'

    mysql = MySQL(app)


    def cadastrarEmail(mysql):
        nome = 'Alexandre'
        email = 'aaaa@aaaa.com'
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO clientes VALUES(%s,%s)''',(nome,email))
        mysql.connection.commit()
        cursor.close()

        return 'Criado com sucesso'




    def atualizar():
        #regra de negocio
        #Banco de dados e atualizando os dados
        return 'Atualizado com sucesso'
