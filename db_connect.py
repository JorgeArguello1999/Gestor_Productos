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
            cur.execute("SELECT clave FROM usuarios WHERE clave=?", (password,))    
            cur.execute("SELECT nombre FROM usuarios WHERE nombre=?", (user_name,))
            print("\nTus credenciales son correctas\n")

        self.conn.close()
        return True 

#Modificamos la tabla de productos
class productos(conexion):

    def listar(self):
        cur = self.conn.cursor()
        pass

    def insertar(self):
        cur = self.conn.cursor()
        pass
        """
        #insert information
        try:
            cur.execute("INSERT INTO usuarios (nombre,clave) VALUES (?, ?)", ("Maria","DB"))
        except mariadb.Error as e:
            print(f"Error: {e}")
        conn.commit()
        """

    def editar(self):
        cur = self.conn.cursor()
        pass

    def eliminar(self):
        cur = self.conn.cursor()
        pass

