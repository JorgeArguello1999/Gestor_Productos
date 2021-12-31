import db_connect
import getpass

class cli:
    def inicio(self):
        print("\nBienvenido al Sistema de Manego de Productos(CLI)\n")
        print("""
        ██▄██ ▄▀▄ █▄░█ █▀▀ ▄▀▀ ▄▀▄ █▀▄ ▄▀▀▄ █▀▄
        █░▀░█ █▄█ █▀██ █▀▀ █░█ █▄█ █░█ █░░█ █▀▄
        ▀░░░▀ ▀░▀ ▀░░▀ ▀▀▀ ░▀▀ ▀░▀ ▀▀░ ░▀▀░ ▀░▀ 

        █▀▄ █▀▀
        █░█ █▀▀
        ▀▀░ ▀▀▀ 

        █▀▄ █▀▄ ▄▀▀▄ █▀▄ █░░█ ▄▀▀ ▀█▀ ▄▀▀▄ ▄▀▀
        █▀░ █▀▄ █░░█ █░█ █░░█ █░░ ░█░ █░░█ ░▀▄
        ▀░░ ▀░▀ ░▀▀░ ▀▀░ ░▀▀░ ░▀▀ ░▀░ ░▀▀░ ▀▀░ 
                """)
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

                # Listar
                if entrada==1:
                    pro.listar()

                # Insertar
                elif entrada==2:
                    pro.listar()
                    codigo= int(input("Ingrese el codigo del producto: "))
                    nombre= input("Ingresa el nombre del producto: ")
                    cantidad= int(input("Ingrese cantidad de producto: "))
                    precio= float(input("Ingrese el precio del producto: "))
                    # Detector de elemento
                    detector= pro.detector(codigo)
                    if detector==True:
                        print("Error (101) El elemento ya existe")
                    else:
                        pro.insertar(codigo, nombre, cantidad, precio)

                # Editar
                elif entrada==3:
                    pro.listar()
                    codigo= int(input("Ingresa el codigo del producto: "))
                    nombre= input("Ingresa el nombre del producto: ")
                    cantidad= int(input("Ingrese cantidad de producto: "))
                    precio= float(input("Ingrese el precio del producto: "))

                    # Detector de elemento
                    detector= pro.detector(codigo)
                    if detector==True:
                        pro.editar(codigo, nombre, cantidad, precio)
                        print("El elemento a modificar existe\n") 
                    else:
                        print("\nError (103) El elemento a modificar no existe")

                # Eliminar
                elif entrada==4:
                    pro.listar()
                    codigo= int(input("Ingresa el ID del producto: ") )
                    nombre= input("Ingresa el nombre del producto: ")
                    
                    entrada= input("Seguro quieres eliminar el contenido? (Si o No)")

                    # Detector de elemento
                    detector= pro.detector(codigo)
                    if entrada=="si" and detector==True or entrada=="Si":
                        pro.eliminar(codigo, nombre)
                    else:
                        print("\nError (102) El elemento a eliminar no existe")

cli().inicio()
