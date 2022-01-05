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
    
            respuesta= cur.execute("SELECT usuario FROM usuarios WHERE usuario=? and clave=?", (user_name,password))
            for nombre in cur:
                print("\nTus credenciales son correctas: ", nombre[0],"\n")
                return True 

        self.conn.close()

#Modificamos la tabla de productos
class productos(conexion):

    #Funcion que lista los contenidos
    def listar(self):
        cur= self.conn.cursor()
        cur.execute("SELECT * FROM productos")
        salida= cur.fetchall()
        for i in salida:
            print("ID: ", i[0])
            print("Nombre: ", i[1])
            print("Cantidad: ", i[2])
            print("Precio:  ", i[3])
            print("\n")
        return salida

    #Funcion que inserta contenido en la tabla
    def insertar(self, codigo, nombre, cantidad, precio):
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO productos (id, nombre, cantidad, precio) VALUES (?, ?, ?, ?)", (codigo, nombre, cantidad, precio))
            print("\nRealizado con exito\n")
        except mariadb.Error as e:
            print(f"Error: {e}")
        self.conn.commit()

    #Funcion que edita los contenidos 
    def editar(self, codigo, nombre, cantidad, precio):
        cur = self.conn.cursor()
        try: 
            cur.execute("UPDATE productos SET id=?, nombre=?, cantidad=?, precio=? WHERE id=?;", (codigo, nombre, cantidad, precio, codigo))
            print("\nEditado con exito")
        except mariadb.Error as e:
            print(f"Error: {e}")

        self.conn.commit()

    #Funcion para eliminar los productos
    def eliminar(self, codigo, nombre):
        cur = self.conn.cursor()
        try:
            cur.execute("DELETE FROM productos WHERE id=? and nombre=?", (codigo, nombre))
            print("\nEliminado con exito: ", nombre) 
        except mariadb.Error as e:
            print(f"Error: {e}")
        self.conn.commit()


    def detector(self, codigo):
        cur= self.conn.cursor()
        cur.execute("SELECT * FROM productos")
        salida= cur.fetchall()
        for i in salida:
            if i[0]==codigo:
                return True
