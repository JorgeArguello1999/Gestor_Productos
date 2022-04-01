import os
import getpass
# Establecemos un path de python para la estructura de paquetes
import Conectors.db_connect as db_connect

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
                self.listador(True)
         
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
                respuesta= self.menu("Insertar")
                pro.insertar(respuesta[0], respuesta[1], respuesta[2], respuesta[3])
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
                codigo= input("Ingrese el codigo del producto a Editar: ")
                nombre= input("Ingrese el nombre del producto a Editar: ")
                print("-------------------------------------------------------")
                print("Editando (Ingrese los nuevos datos) >> ADVERTENCIA NO CAMBIAR EL ID")
                respuesta= self.menu("Editar")
                pro.editar(codigo, nombre, respuesta[1], respuesta[2], respuesta[3])
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
                    
                entrada= input("Seguro quieres eliminar el contenido? (Si o No): ")
                if entrada=="si" or entrada=="Si":
                    pro.eliminar(codigo, nombre)

                self.salida()

    def menu(self, mensaje):
        codigo= int(input(f"Ingresa el codigo del producto a {mensaje}: "))
        nombre= input(f"Ingresa el nombre del producto a {mensaje}: ")
        cantidad= int(input(f"Ingrese cantidad de producto a {mensaje}: "))
        precio= float(input(f"Ingrese el precio del producto a {mensaje}: "))
        respuestas=(
                codigo,
                nombre,
                cantidad,
                precio,
                )
        return respuestas
        



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
            2.- Editar Usuarios
            3.- Eliminar Usuarios
                    """)
            accion= int(input("Tu eleccion: "))
            if accion==1:
                respuestas= self.menu_admin("Insertar")
                con.insertar(respuestas[0], respuestas[1], respuestas[2], respuestas[3])
            elif accion==3:
                id_usuario= int(input("Ingrese el ID del usuario a Editar:  "))
                user_name= input("Ingrese el nombre del usuario a Editar: ")
                print("-----------------------------------------------------------------")
                print("Inserte los datos del usuario a Editar >> ADVERTENCIA no cambiar el ID")
                respuestas= self.menu_admin("Eliminar")
                con.editar(id_usuario, user_name, respuestas[1], respuestas[2], respuestas[3])
            elif accion==2:
                respuestas= self.menu_admin("Eliminar")
                con.eliminar(respuestas[0], respuestas[1], respuestas[2], respuestas[3])
            self.limpiador()
    
    def menu_admin(self, accion):
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
