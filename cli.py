import db_connect
import getpass

class cli:
    def inicio(self):
        print("\nBienvenido al Sistema de Manego de Productos(CLI)\n")
        user= input("Ingresa tu usuario: ")
        password= getpass.getpass('Ingresa tu contraseña: ') 

        if user!=None and password!=None:
            con=db_connect.conexion()
            respuesta=con.verificador(user, password)
         
            if respuesta==True:
                print("""
                1.- Listar articulos
                2.- Insertar articulos
                3.- Editar ariticulos
                4.- Eliminar articulos
                        """)
                self.entrada= input("Tu eleccion: ")
                return self.entrada

    def selector(self):
        pro= db_connect.productos()

        if self.entrada==1:
            pro.listar()
        elif self.entrada==2:
            pro.insertar()
        elif self.entrada==3:
            pro.editar()
        elif self.entrada==4:
            pro.eliminar()



cli().inicio()
