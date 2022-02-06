# Este modulo es solo para la conexion de la base de datos
#!/usr/bin/python
import mariadb
import crypt

class conexion:
    #Verificacion de usuario
    def __init__(self):
        self.conn = mariadb.connect(
            user="jorge",
            password="basededatos",
            host="192.168.1.8",
            database="aplicacion"
            )

    # Solucionar no paso el login
    def verificador(self, user_name, password):
        cur = self.conn.cursor()
        clave= crypt.crypt(password, user_name)
        # print(clave)
        #Reciviendo informacion y validando
        if user_name != None and password != None:
            cur.execute("SELECT * FROM usuarios WHERE usuario=? and clave=?", (user_name, clave))
            for nombre in cur:
                print("\nTus credenciales son correctas: ", nombre[1],"\n")
                self.conn.close()
                return True 

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
            #insert into productos(id, nombre, cantidad, precio)  select 99, "Hijo", 9, 9.90 where not exists(select 99 from productos where nombre="Hijo" );
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


    def detector(self, codigo, nombre):
        cur= self.conn.cursor()
        cur.execute("SELECT * FROM productos")
        salida= cur.fetchall()
        for i in salida:
            if i[0]==codigo or i[1]==nombre:
                return True


class usuarios(conexion):
    def insertar(self, id_usuario, user_name, password, area):
        cur= self.conn.cursor()
        clave= crypt.crypt(password, user_name)
        try:
            cur.execute( "INSERT INTO usuarios (id_usuario, usuario, clave, area) VALUES (?, ?, ?, ?);",(id_usuario, user_name, clave, area) )
            print("Se ingreso el usuario: ", user_name)
        except mariadb.Error as e: 
            print(f"Error: {e}")
        self.conn.commit()
    
    def eliminar(self, id_usuario, user_name, password, area):
        cur= self.conn.cursor()
        clave= crypt.crypt(password, user_name)
        try:
            cur.execute( "DELETE FROM usuarios WHERE id_usuario=? and usuario=? and clave=? and area=?",(id_usuario, user_name, clave, area) )
            print("Se elimino el usuario: ", user_name)
        except mariadb.Error as e:
            print(f"Error: {e}")
        self.conn.commit()

    def editar(self, id_usuario, user_name, password, area):
        cur= self.conn.cursor()
        clave= crypt.crypt(password, user_name)
        try:
            cur.execute( "UPDATE usuarios SET id_usuario=?, usuario=?, clave=?, area=?", (id_usuario, user_name, clave, area) )
            print("Editado el usuario: ", user_name)
        except mariadb.Error as e:
            print(f"Error: {e}")
        self.conn.commit()
