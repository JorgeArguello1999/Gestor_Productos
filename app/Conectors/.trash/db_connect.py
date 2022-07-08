# Este modulo es solo para la conexion de la base de datos
import mariadb

class conexion:
    #Verificacion de usuario
    def __init__(self):
        self.conn = mariadb.connect(
            user="root",
            password="root",
            host="192.168.1.13",
            database="aplicacion"
            )
    def encriptador(self, user_name, password):
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
    def detector(self, user_name, clave, area):
        cur= self.conn.cursor()
        try:
            cur.execute("SELECT * FROM usuarios")
            for date in cur:
                if date[1]==user_name and date[2]==clave and date[3]==area:
                    print("Existe")
                    return True
        except mariadb.Error as e:
            print(f"Error: {e}")


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
        except mariadb.Error as e: 
            print(f"Error: {e}")

    # Modificar este segmento ya que mantiene la informacion añadir entradas para nuevos datos de usuario 
    def editar(self, id_usuario, user_name, new_user_name, password, area):
        cur= self.conn.cursor()
        clave= self.encriptador(user_name, password)
        detec= self.detector(id_usuario, user_name, clave )
        if detec==True:
            try: 
                sql= "UPDATE usuarios SET id_usuario=%s, usuario=%s, clave=%s, area=%s WHERE id_usuario=%s"
                cur.execute(sql, (id_usuario, user_name, clave, area, id_usuario))
                print(f"Usuario: {user_name} actualizado")
                self.conn.commit()
                return True
            except mariadb.Error as e:
                print(f"Error: {e}")

    def eliminar(self, id_usuario, user_name, password, area):
        cur= self.conn.cursor()
        clave= self.encriptador(user_name, password)
        detec= self.detector(id_usuario, user_name, clave)
        if detec==True:
            try:
                sql= "DELETE FROM usuarios WHERE id_usuario=%s and usuario=%s and clave=%s and area=%s"
                cur.execute(sql, (id_usuario, user_name, clave, area))
                print(f"Se elimino el usuario: {user_name}")
                self.conn.commit()
                return True
            except mariadb.Error as e:
                print(f"Error: {e}")

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

    def mate(self, cantidad, precio):
        return cantidad*precio

    #Funcion que lista los contenidos
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
        except mariadb.Error as e:
            print(f"Error: {e}")

    #Funcion que inserta contenido en la tabla
    def insertar(self, nombre, cantidad, precio):
        cur = self.conn.cursor()
        try:
            #insert into productos(id, nombre, cantidad, precio)  select 99, "Hijo", 9, 9.90 where not exists(select 99 from productos where nombre="Hijo" );
            precio_productos= self.mate(cantidad, precio)
            cur.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES ( ?, ?, ?)", (nombre, cantidad, precio_productos))
            print("\nRealizado con exito\n")

        except mariadb.Error as e:
            print(f"Error: {e}")
        self.conn.commit()

    #Funcion que edita los contenidos 
    def editar(self, codigo, nombre, cantidad, precio):
        cur = self.conn.cursor()
        precio_productos= self.mate(cantidad, precio)
        try: 
            cur.execute("UPDATE productos SET id=?, nombre=?, cantidad=?, precio=? WHERE id=?;", (codigo, nombre, cantidad, precio_productos, codigo))
            print("\nEditado con exito")
        except mariadb.Error as e:
            print(f"Error: {e}")

        self.conn.commit()

    #Funcion para eliminar los productos
    def eliminar(self, codigo):
        cur = self.conn.cursor()
        try:
            cur.execute(f"DELETE FROM productos WHERE id={codigo}")
            print("\nEliminado con exito: ", codigo ) 
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
