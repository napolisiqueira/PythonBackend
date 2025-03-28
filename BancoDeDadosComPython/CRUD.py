import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    conn = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
    cur = conn.cursor()

    def create_table (conn, cur, nome, email):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS  clientes
            (
                id INTEGER PRIMARY KEY,
                nome VARCHAR(100),
                email VARCHAR(150)
            )
        ''')

    Whatsapp = input("Digite o Whatsapp: ")
    Telefone = input("Digite o telefone: ")
    Email = input("Digite o email: ")
    data = (Whatsapp, Telefone, Email)


    cur.execute("INSERT INTO clientes (nome, email) VALUES(?, ?)", data)

finally:
    conn.commit()
    conn.close()