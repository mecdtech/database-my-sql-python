import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha",
  database="seu_banco_de_dados"
)

mycursor = mydb.cursor()

sql = "INSERT INTO clientes (nome, endereco) VALUES (%s, %s)"
val = ("João", "Rua A, 123")
mycursor.execute(sql, val)
mydb.commit()
mydb.close()
