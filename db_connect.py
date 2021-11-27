# Este modulo es solo para la conexion de la base de datos
#!/usr/bin/python
import mariadb

conn = mariadb.connect(
    user="root",
    password="",
    host="localhost",
    database="aplicacion")

cur = conn.cursor()

#retrieving information
some_name = "Georgi"
cur.execute("SELECT nombre FROM usuarios WHERE nombre=?", (some_name,))

for nombre in cur:
    print(f"First name: {nombre}")

#insert information
try:
    cur.execute("INSERT INTO usuarios (nombre,clave) VALUES (?, ?)", ("Maria","DB"))
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")

conn.close()
