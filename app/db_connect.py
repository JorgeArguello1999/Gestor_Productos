import pymysql
import crypt

from pymysql.err import Error

class conexion:
    def __init__(self):
        self.conn= pymysql.connect(
                host= '127.0.0.1',
                user= 'jorge',
                password= 'basededatos',
                database= 'aplicacion',
                )

    def encriptador(self, user_name, password):
        return crypt.crypt(password, user_name)

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
            return True
        # En caso de ocurrir un Error
        except pymysql.Error as e: 
            print(f"Error: {e}")
        self.conn.commit()

    # Modificar este segmento ya que mantiene la informacion añadir entradas para nuevos datos de usuario 
    def editar(self, id_usuario, user_name, password, area):
        cur= self.conn.cursor()
        clave= self.encriptador(user_name, password)
        detector= self.detector(id_usuario, user_name, clave, area)
        if detector==True:
            try: 
                sql= "UPDATE usuarios SET id_usuario=%s, usuario=%s, clave=%s, area=%s"
                cur.execute(sql, (id_usuario, user_name, clave, area))
                print(f"Usuario: {user_name} actualizado")
                return True
            except pymysql.Error as e:
                print(f"Error: {e}")
    
    def eliminar(self, id_usuario, user_name, password, area):
        cur= self.conn.cursor()
        clave= self.encriptador(user_name, password)
        detector= self.detector(id_usuario, user_name, clave, area)
        if detector==True:
            try:
                sql= "DELETE FROM usuarios WHERE id_usuario=? and usuario=%s and clave=%s and area=%s"
                cur.execute(sql, (id_usuario, user_name, clave, area))
                print(f"Se elimino el usuario: {user_name}")
                return True
            except pymysql.Error as e:
                print(f"Error: {e}")

    def detector(self, id_usuario, user_name, clave, area):
        cur= self.conn.cursor()
        try:
            cur.execute("SELECT * FROM usuarios")
            for date in cur:
                if date[0]==id_usuario and date[1]==user_name and date[2]==clave and date[3]==area:  
                    print("Existe")
                    return True
        except pymysql.Error as e:
            print(f"Error: {e}")

class productos(conexion):
    pass
