# Este modulo es solo para la conexion de la base de datos
#!/usr/bin/python
import mariadb

class conexion:
    #Verificacion de usuario
    def __init__(self, user_name, password):

        self.conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            database="aplicacion"
            )

        cur = self.conn.cursor()

        #Reciviendo informacion y validando
        if user_name != None and password != None:

            cur.execute("SELECT nombre FROM usuarios WHERE nombre=?", (user_name,))
            for nombre in cur:
                print(f"Tu usuario es correcto")

            cur.execute("SELECT clave FROM usuarios WHERE clave=?", (password,))    
            for clave in cur:
                print(f"Tu usuario es correcto")

        self.conn.close()

    def insert(self):
        pass
        """
        #insert information
        try:
            cur.execute("INSERT INTO usuarios (nombre,clave) VALUES (?, ?)", ("Maria","DB"))
        except mariadb.Error as e:
            print(f"Error: {e}")
        conn.commit()
        """

conexion('Georgi', 'Ninguna')
