import db_connect
import os
import getpass


class cli:

    def salida(self):
        salida= input("Quieres Salir: S/N ")
        if salida=="N" or salida=="n":
            self.listador(respuesta=True)
            self.limpiador()
        else:
            os.system("exit")

    def limpiador(self):
        command= "clear"
        if os.name in ('nt', 'dos'):
            command= "cls"
        os.system(command)

    def main(self):
        self.limpiador()
        print("\nBienvenido al Sistema de Gestion de Productos(CLI)\n")
        print("""
               ▄▀▀ █▀▀ ▄▀▀ ▀█▀ ▄▀▀▄ █▀▄
               █░█ █▀▀ ░▀▄ ░█░ █░░█ █▀▄
               ░▀▀ ▀▀▀ ▀▀░ ░▀░ ░▀▀░ ▀░▀ 
       
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

            # respuesta=con.verificador(user, password)
            # Verificamos si eres ADMIN
            admin= con.admin(user, password)
            if admin==True:
                self.admin()
                # Iniciamos el modulo de listar 
                self.listador(True)
            elif admin==False:
                self.listador(False)
         
    def listador(self, respuesta):
        if respuesta==True:
            print("""
            Elije la opcion a realizar...
            1.- Listar articulos
            2.- Insertar articulos
            3.- Editar ariticulos
            4.- Eliminar articulos
            """)
            entrada= int(input("Tu eleccion: "))
            self.limpiador()

            pro= db_connect.productos()

            # Listar
            if entrada==1:
                print("""
                         █░░ ▀█▀ ▄▀▀ ▀█▀ ▄▀▄ █▀▄
                         █░░ ░█░ ░▀▄ ░█░ █▄█ █▀▄
                         ▀▀▀ ▀▀▀ ▀▀░ ░▀░ ▀░▀ ▀░▀ 
                    ▄▀▄ █▀▄ ▀█▀ ▀█▀ ▄▀▀ █░░█ █░░ ▄▀▀▄ ▄▀▀
                    █▄█ █▀▄ ░█░ ░█░ █░░ █░░█ █░░ █░░█ ░▀▄
                    ▀░▀ ▀░▀ ░▀░ ▀▀▀ ░▀▀ ░▀▀░ ▀▀▀ ░▀▀░ ▀▀░ 
                """)
                pro.listar()
                self.salida()

            # Insertar
            elif entrada==2:
                print("""
                      ▀█▀ █▄░█ ▄▀▀ █▀▀ █▀▄ ▀█▀ ▄▀▄ █▀▄
                      ░█░ █▀██ ░▀▄ █▀▀ █▀▄ ░█░ █▄█ █▀▄
                      ▀▀▀ ▀░░▀ ▀▀░ ▀▀▀ ▀░▀ ░▀░ ▀░▀ ▀░▀ 
                    ▄▀▄ █▀▄ ▀█▀ ▀█▀ ▄▀▀ █░░█ █░░ ▄▀▀▄ ▄▀▀
                    █▄█ █▀▄ ░█░ ░█░ █░░ █░░█ █░░ █░░█ ░▀▄
                    ▀░▀ ▀░▀ ░▀░ ▀▀▀ ░▀▀ ░▀▀░ ▀▀▀ ░▀▀░ ▀▀░ 
                """)
                pro.listar()
                codigo= int(input("Ingrese el codigo del producto: "))
                nombre= input("Ingresa el nombre del producto: ")
                cantidad= int(input("Ingrese cantidad de producto: "))
                precio= float(input("Ingrese el precio del producto: "))
                # Detector de elemento
                detector= pro.detector(codigo, nombre)
                if detector==True:
                    print("Error (101) El elemento ya existe")
                else:
                    pro.insertar(codigo, nombre, cantidad, precio)
                self.salida()

            # Editar
            elif entrada==3:
                print("""
                    
                           █▀▀ █▀▄ ▀█▀ ▀█▀ ▄▀▄ █▀▄
                           █▀▀ █░█ ░█░ ░█░ █▄█ █▀▄
                           ▀▀▀ ▀▀░ ▀▀▀ ░▀░ ▀░▀ ▀░▀ 
                    ▄▀▄ █▀▄ ▀█▀ ▀█▀ ▄▀▀ █░░█ █░░ ▄▀▀▄ ▄▀▀
                    █▄█ █▀▄ ░█░ ░█░ █░░ █░░█ █░░ █░░█ ░▀▄
                    ▀░▀ ▀░▀ ░▀░ ▀▀▀ ░▀▀ ░▀▀░ ▀▀▀ ░▀▀░ ▀▀░ 
                """)
                pro.listar()
                codigo= int(input("Ingresa el codigo del producto: "))
                nombre= input("Ingresa el nombre del producto: ")
                cantidad= int(input("Ingrese cantidad de producto: "))
                precio= float(input("Ingrese el precio del producto: "))

                # Detector de elemento
                detector= pro.detector(codigo, nombre)
                if detector==True:
                    pro.editar(codigo, nombre, cantidad, precio)
                    print("El elemento a modificar existe\n") 
                else:
                    print("\nError (103) El elemento a modificar no existe")
                self.salida()

            # Eliminar
            elif entrada==4:
                print("""
                      █▀▀ █░░ ▀█▀ ██▄██ ▀█▀ █▄░█ ▄▀▄ █▀▄
                      █▀▀ █░░ ░█░ █░▀░█ ░█░ █▀██ █▄█ █▀▄
                      ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀ ▀▀▀ ▀░░▀ ▀░▀ ▀░▀ 
                    ▄▀▄ █▀▄ ▀█▀ ▀█▀ ▄▀▀ █░░█ █░░ ▄▀▀▄ ▄▀▀
                    █▄█ █▀▄ ░█░ ░█░ █░░ █░░█ █░░ █░░█ ░▀▄
                    ▀░▀ ▀░▀ ░▀░ ▀▀▀ ░▀▀ ░▀▀░ ▀▀▀ ░▀▀░ ▀▀░ 
                """)
                pro.listar()
                codigo= int(input("Ingresa el ID del producto: ") )
                nombre= input("Ingresa el nombre del producto: ")
                    
                entrada= input("Seguro quieres eliminar el contenido? (Si o No)")

                # Detector de elemento
                detector= pro.detector(codigo, nombre)
                if entrada=="si" and detector==True or entrada=="Si":
                    pro.eliminar(codigo, nombre)
                else:
                    print("\nError (102) El elemento a eliminar no existe")
                self.salida()

    def admin(self):
        self.limpiador()
        con= db_connect.usuarios()
        print("""
            ▄▀▀ █▀▀ ▄▀▀ ▀█▀ ▀█▀ ▄▀▀▄ █▄░█
            █░█ █▀▀ ░▀▄ ░█░ ░█░ █░░█ █▀██
            ░▀▀ ▀▀▀ ▀▀░ ░▀░ ▀▀▀ ░▀▀░ ▀░░▀

           █░░█ ▄▀▀ █░░█ ▄▀▄ █▀▄ ▀█▀ ▄▀▀▄ ▄▀▀
           █░░█ ░▀▄ █░░█ █▄█ █▀▄ ░█░ █░░█ ░▀▄
           ░▀▀░ ▀▀░ ░▀▀░ ▀░▀ ▀░▀ ▀▀▀ ░▀▀░ ▀▀░ 
                """)
        print("""
        1,. Gestor de usuarios 
        2.- Gestor de Productos
        """)
        entrada= int(input("Tu eleccion: "))
        if entrada==1:
            print("""
            1.- Insertar Usuarios
            2.- Eliminar Usuarios
            3.- Editar Usuarios
                    """)
            accion= int(input("Tu eleccion: "))
            if accion==1:
                respuestas= self.menu("Insertar")
                con.insertar(respuestas[0], respuestas[1], respuestas[2], respuestas[3])
            elif accion==2:
                respuestas= self.menu("Eliminar")
                detector= con.detector(respuestas[0], respuestas[1], respuestas[2], respuestas[3])
                if detector==True:
                    con.eliminar(respuestas[0], respuestas[1], respuestas[2], respuestas[3])
            elif accion==3:
                respuestas= self.menu("Editar")
                detector= con.detector(respuestas[0], respuestas[1], respuestas[2], respuestas[3])
                if detector==True:
                    con.editar(respuestas[0], respuestas[1], respuestas[2], respuestas[3])
        self.limpiador()
    
    def menu(self, accion):
        id_usuario= input(f"Ingrese el ID del usuario a {accion}: ")
        user_name= input(f"Ingrese el nombre del usuario a {accion}: ")
        password= input(f"Ingrese la contraseña del usuario a {accion}: ")
        area= input(f"Ingrese el area de trabajo del usuario a {accion}: ")
        respuestas=(
                id_usuario,
                user_name,
                password,
                area,
                )
        return respuestas


if __name__=='__main__':
    aplicacion= cli()
    aplicacion.main()
    
