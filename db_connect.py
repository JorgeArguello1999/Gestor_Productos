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
    #Funcion que lista los contenidos
    def listar(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM productos")
        self.salida= cur.fetchall()
        for i in self.salida:
            print(i)
        return self.salida

    #Funcion que inserta contenido en la tabla
    def insertar(self, codigo, nombre, cantidad, precio):
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO productos (id, nombre, cantidad, precio) VALUES (?, ?, ?, ?)", (codigo, nombre, cantidad, precio))
            print("\nRealizado con exito\n")
        except mariadb.Error as e:
            print(f"Error: {e}")
        self.conn.commit()
        return self.salida 

    #Funcion que edita los contenidos 
    def editar(self):
        cur = self.conn.cursor()
        pass

    #Funcion para eliminar los productos
    def eliminar(self, codigo, nombre):
        cur = self.conn.cursor()
        try:
            productos= self.listar()
            for i in productos:
                print(i)
            cur.execute("DELETE FROM productos WHERE ? =?; AND ?=?"), (codigo, nombre)
        except mariadb.Error as e:
            print(f"Error: {e}")
        self.conn.commit()
        return print("Eliminado: ?"), (nombre)

    def detector(self):
        pass
