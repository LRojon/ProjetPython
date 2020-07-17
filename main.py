#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import os
from flask import Flask, request, current_app, g, render_template
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
import sqlite3


class Boutique(Resource):

    def post(self, typex, command):
        if typex == 'produits':
            if command == 'get':
                conn = sqlite3.connect('boutique.db')
                cur = conn.cursor()
                result = cur.execute('select * from produit')
                r = []
                for row in result:
                    r.append({
                        'id': row[0],
                        'nom': row[1],
                        'description': row[2],
                        'prix': row[3],
                        })
                return {'data': r}

            elif command == "set":
                nom = request.json['nom']
                desc = request.json['description']
                prix = request.json['prix']
                conn = sqlite3.connect('boutique.db')
                cur = conn.cursor()
                cur.execute('select * from produit where nom= ? and ' +
                            'description= ?', (nom, desc))
                if cur.fetchone() is None:
                    cur.execute('insert into produit(nom, description, prix)' +
                                'values(?, ?, ?)', (nom, desc, prix))
                    conn.commit()
                    return {'code': 200}
                else:
                    return {'code': 500}
        return {'code': 500}


class User(Resource):

    def post(self, command):
        if command == "login":
            login = request.json['login']
            password = request.json['password']
            conn = sqlite3.connect('boutique.db')
            cur = conn.cursor()
            cur.execute('select * from client where login= ? and password= ?',
                        (login, password))
            row = cur.fetchone()
            if row is None:
                return {'code': 500}
            else:
                return {'code': 200}

        elif command == "get":
            login = request.json['login']
            conn = sqlite3.connect('boutique.db')
            cur = conn.cursor()
            cur.execute('select * from client where login= ?',
                        (login,))
            row = cur.fetchone()
            if row is None:
                return {'code': 500}
            else:
                return {
                        'id': row[0],
                        'login': row[1],
                        'nom': row[2],
                        'prenom': row[3],
                        'role': row[5]
                        }

        elif command == "signup":
            login = request.json['login']
            nom = request.json['nom']
            prenom = request.json['prenom']
            password = request.json['password']
            confirm = request.json['confirm']
            conn = sqlite3.connect('boutique.db')
            cur = conn.cursor()
            if confirm == password:
                cur.execute('select * from client where login= ?',
                            (login,))
                row = cur.fetchone()
                if row is None:
                    cur.execute('insert into client(login, nom, prenom, ' +
                                'password, role) values(?, ?, ?, ?, ?)',
                                (login, nom, prenom, password, "user"))
                    conn.commit()
                    return {'code': 200, 'message': 'OK'}
                else:
                    return {'code': 500, 'message': 'Pseudo déjà utilisé.'}
            else:
                return {'code': 500, 'message': 'Les mots de passe ne ' +
                        'correspondent pas.'}


class Server:

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(Boutique, '/<typex>/<command>')
        self.api.add_resource(User, '/user/<command>')

        @self.app.after_request
        def after_request(response):
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers',
                                 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods',
                                 'GET,PUT,POST,DELETE,OPTIONS')
            return response

        @self.app.route("/")
        def index():
            return render_template("index.html")

        @self.app.route("/shop/<login>")
        def shop(login):
            return render_template("shop.html", login=login)

        @self.app.route("/signup")
        def signup():
            return render_template("signup.html")

        @self.app.route("/admin")
        def admin():
            return render_template("admin.html")

    def start(self):
        self.app.run()


s = Server()
s.start()
