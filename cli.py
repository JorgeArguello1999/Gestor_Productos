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
                    pro.listar()

                elif entrada==2:
                    codigo= int(input("Ingrese el codigo del producto: "))
                    nombre= input("Ingresa el nombre del producto: ")
                    cantidad= int(input("Ingrese cantidad de producto: "))
                    precio= float(input("Ingrese el precio del producto: "))
                    pro.insertar(codigo, nombre, cantidad, precio)

                elif entrada==3:
                    pro.editar()
                elif entrada==4:
                    pro.listar()
                    codigo= int(input("Ingresa el ID del producto: ") )
                    nombre= input("Ingresa el nombre del producto: ")
                    
                    entrada= input("Seguro quieres eliminar el contenido? (Si o No)")
                    if entrada=="si":
                        pro.eliminar(codigo, nombre)


cli().inicio()
