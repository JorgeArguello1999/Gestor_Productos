# Este modulo es solo para la conexion de la base de datos
#!/usr/bin/python
import mariadb

class conexion:
    #Verificacion de usuario
    def __init__(self):
        self.conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            database="aplicacion"
            )

    def verificador(self, user_name, password):
        cur = self.conn.cursor()

        #Reciviendo informacion y validando
        if user_name != None and password != None:
    
            respuesta= cur.execute("SELECT nombre FROM usuarios WHERE nombre=? and clave=?", (user_name,password))
            for nombre in cur:
                print(f"\nTus credenciales son correctas: {nombre}\n")
                return True 



        self.conn.close()

#Modificamos la tabla de productos
class productos(conexion):
    def listar(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM productos")
        salida= cur.fetchall()
        return print(salida)

    def insertar(self, codigo, nombre, cantidad, precio):
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO productos (id, nombre, cantidad, precio) VALUES (?, ?, ?, ?)", (codigo, nombre, cantidad, precio))
            print("\nRealizado con exito\n")
        except mariadb.Error as e:
            print(f"Error: {e}")
        self.conn.commit()
        return print(self.listar() )

    def editar(self):
        cur = self.conn.cursor()
        pass

    def eliminar(self):
        cur = self.conn.cursor()
        pass

