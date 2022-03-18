import sqlite3
import json

JSON = 'rezultati.txt'

DB = sqlite3.connect('top.db')
SQL = DB.cursor()

SQL.execute("""CREATE TABLE IF NOT EXISTS rezultati ( 
              id INTEGER NOT NULL UNIQUE,
              vards TEXT,
              punkti INTEGER,
              PRIMARY KEY("id" AUTOINCREMENT)
           )""")

with open(JSON, 'r', encoding="UTF-8") as f:
  dati = f.read()
  datiJson = json.loads(dati)

  for dati in datiJson:
    SQL.execute("INSERT INTO rezultati (vards, punkti) VALUES (:vards, :punkti)", {'vards': dati['vards'], 'punkti': dati['punkti']})


DB.commit()

SQL.execute("SELECT * FROM rezultati")

print(SQL.fetchall())
    