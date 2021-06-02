from flask import Flask
from conexao import connect
from flask_jsonpify import jsonify

app = Flask(__name__) 

@app.route("/clientes")
def get_clientes():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('select CustomerId, FirstName, LastName from customers')
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names, i)) for i in records]
    conn.close()
    return jsonify(lista)

@app.route("/cliente/<id>")
@app.route("/clientes/<id>")
def get_client_by_id(id:int):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f'select CustomerId, FirstName, LastName, Address, City, State, Country from customers where CustomerId = {id}')
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names, i)) for i in records]
    conn.close()
    return jsonify(lista)

app.run(port=8080, debug=True)