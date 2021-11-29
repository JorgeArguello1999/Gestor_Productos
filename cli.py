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
                Elije la opcion a realizar...
                1.- Listar articulos
                2.- Insertar articulos
                3.- Editar ariticulos
                4.- Eliminar articulos
                        """)
                entrada= int(input("Tu eleccion: "))

                pro= db_connect.productos()

                if entrada==1:
                    print(pro.listar())
                elif entrada==2:
                    print(pro.insertar(3, 'Nombre', 8, 9))
                elif entrada==3:
                    pro.editar()
                elif entrada==4:
                    pro.eliminar()



cli().inicio()
