import sqlite3
import json
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conn = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
cur = conn.cursor()
cur.row_factory = sqlite3.Row



def create_table(conn, cur):
    cur.execute('''
    CREATE TABLE IF NOT EXISTS  clientes
        (
            id INTEGER PRIMARY KEY,
            nome VARCHAR(100),
            email VARCHAR(150),
            whatsapp INTEGER,
            telefone INTEGER
        )
    ''')

def delete_data(conn, cur, id):
    cur.execute("DELETE FROM clientes WHERE id= '?'", id)

def update_data(conn, cur, id, args*):
    #upgrade this code to no aceppt break SQL injection.
    sqlinjection = args
    cur.execution("UPDATE sqlinjection INTO clientes WHERE id = '?'", args)

def insert_new(conn, cur):

    Name = input("Digite o Nome: ")
    Whatsapp = input("Digite o Whatsapp: ")
    Telefone = input("Digite o telefone: ")
    Email = input("Digite o email: ")
    data = (Name, Whatsapp, Telefone, Email)
    cur.execute("INSERT INTO clientes (nome, email, telefone, whatsapp) VALUES(?, ?, ?, ?)", data)

def insert_much(conn, cur, archive):

    with open (archive, 'r', encoding="utf-8") as file:
        jsonfile = [json.load(file)]

    cur.executemany('INSERT INTO clientes (nome, email, telefone, whatsapp) VALUES(?, ?, ?, ?)", jsonfile')

def serach_one(conn, cur, id):
    cur.execute("SELECT FROM clientes BY id= '?'", id)
    print(cur.fetchone())

def searsh_all(conn, cur):
    cur.execute("SELECT FROM clientes")
    print(cur.fethmany())

conn.commit()
conn.close()