import pymysql
import crypt

from pymysql.err import Error

class conexion:
    def __init__(self):
        # Configurar esta parte para que sea facilmente cambiable
        self.conn= pymysql.connect(
                host= '192.168.1.13',
                user= 'root',
                password= 'root',
                database= 'aplicacion',
                )

    def encriptador(self, user_name, password):
        # Este modulo debe ser modificado para que sea usable desde cualquier sistema operativo
        # El modulo crypt solo esta disponible para sistemas UNIX, windows no funciona
        return (password, user_name)

    def admin(self, user_name, password):
        # Inicia la conexion
        cur= self.conn.cursor()
        # Encriptamos la clave a traves del metodo "encriptador"
        clave= self.encriptador(user_name, password)
        # Hacemos la busqueda en la Base de Datos
        cur.execute("SELECT * FROM usuarios WHERE usuario=%s and clave=%s", (user_name, clave))
        # Comprobamos si es ADMIN
        for admin in cur:
            if user_name != None and password != None and admin[1]==user_name and admin[2]==clave:
                if admin[3]!='admin':
                    print("\nHola:", admin[1], "tus credenciales son correctas\n")
                    return False
                elif admin[3]=='admin':
                    print("\nHola:", admin[1], "eres un ADMIN\n")
                    return True
        # Terminamos la conexion
        self.conn.close()

class usuarios(conexion):
    def insertar(self, id_usuario, user_name, password, area):
        cur= self.conn.cursor()
        clave= self.encriptador(user_name, password)
        # Se intenta insertar el nuevo usuario
        try:
            sql= "INSERT INTO usuarios (id_usuario, usuario, clave, area) VALUES (%s, %s, %s, %s)"
            cur.execute(sql,(id_usuario, user_name, clave, area))
            print("Se ingreso el usuario: ", user_name)
            self.conn.commit()
            return True
        # En caso de ocurrir un Error
        except pymysql.Error as e: 
            print(f"Error: {e}")

    # Modificar este segmento ya que mantiene la informacion añadir entradas para nuevos datos de usuario 
    def editar(self, id_usuario, user_name, new_user_name, password, area):
        cur= self.conn.cursor()
        clave= self.encriptador(user_name, password)
        detector= self.detector(id_usuario, user_name, clave, area)
        if detector==True:
            try: 
                sql= "UPDATE usuarios SET id_usuario=%s, usuario=%s, clave=%s, area=%s WHERE id_usuario=%s"
                cur.execute(sql, (id_usuario, user_name, clave, area, id_usuario))
                print(f"Usuario: {user_name} actualizado")
                self.conn.commit()
                return True
            except pymysql.Error as e:
                print(f"Error: {e}")

    def eliminar(self, id_usuario, user_name, password, area):
        cur= self.conn.cursor()
        clave= self.encriptador(user_name, password)
        detector= self.detector(id_usuario, user_name, clave, area)
        if detector==True:
            try:
                sql= "DELETE FROM usuarios WHERE id_usuario=%s and usuario=%s and clave=%s and area=%s"
                cur.execute(sql, (id_usuario, user_name, clave, area))
                print(f"Se elimino el usuario: {user_name}")
                self.conn.commit()
                return True
            except Error as e:
                print(f"Error: {e}")

    def detector(self, user_name, clave, area):
        cur= self.conn.cursor()
        try:
            cur.execute("SELECT * FROM usuarios")
            for date in cur:
                if date[1]==user_name and date[2]==clave and date[3]==area:
                    print("Existe")
                    return True
        except pymysql.Error as e:
            print(f"Error: {e}")

class productos(conexion):
    def listar(self):
        cur=self.conn.cursor()
        try:
            cur.execute("SELECT * FROM productos")
            salida= cur.fetchall()
            datos=[]
            for productos in salida:
                print("\n")
                print(f"""
            *-----------*-------------------------------------------*
            | ID        | {productos[0]}
            *-----------*-------------------------------------------*
            | Nombre    | {productos[1]}
            *-----------*-------------------------------------------*
            | Cantidad  | {productos[2]}
            *-----------*-------------------------------------------*
            | Precio    | {productos[3]}
            *-----------*-------------------------------------------*
                        """)
                datos.append(productos)
            print(datos)
            return datos 
        except pymysql.Error as e:
            print(f"Error: {e}")

    def insertar(self, codigo, nombre, cantidad, precio):
        cur= self.conn.cursor()
        detector= self.detector(codigo, nombre)
        try:
            if detector!=True:
                sql= "INSERT INTO productos (id, nombre, cantidad, precio) VALUES (%s, %s, %s, %s)"
                cur.execute(sql, (codigo, nombre, cantidad, precio))
                self.conn.commit()
                print("Realizado con exito")
                return True
        except pymysql.Error as e:
            print(f"Error: {e}")

    # Modificar para ingresar nueva información solo hacemos redundancia
    def editar(self, codigo, nombre, nuevo_nombre, nuevo_cantidad, nuevo_precio):
        cur= self.conn.cursor()
        detector= self.detector(codigo, nombre)
        try: 
            if detector==True:
                sql= "UPDATE productos SET id=%s, nombre=%s, cantidad=%s, precio=%s WHERE id=%s"
                cur.execute(sql, (codigo, nuevo_nombre, nuevo_cantidad, nuevo_precio, codigo))
                self.conn.commit()
                print("Editado con exito")
                return True
        except pymysql.Error as e:
            print(f"Error: {e}")

    def eliminar(self, codigo, nombre):
        cur= self.conn.cursor()
        detector= self.detector(codigo, nombre)
        try:
            if detector==True:
                sql= "DELETE FROM productos WHERE id=%s and nombre=%s"
                cur.execute(sql, (codigo, nombre))
                print("Eliminado con exito")
                self.conn.commit()
                return True
        except pymysql.Error as e:
            print(f"Error: {e}")

    def detector(self, codigo, nombre):
        cur= self.conn.cursor()
        try:
            sql= "SELECT * FROM productos"
            cur.execute(sql)
            salida= cur.fetchall()
            for productos in salida:
                if productos[0]==codigo or productos[1]==nombre:
                    return True
        except pymysql.Error as e:
            print(f"Error: {e}")
