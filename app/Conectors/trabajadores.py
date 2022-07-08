import init
import requests
import json

class trabajadores(init.conexion):
    def __init__(self):
        global URL
        URL = self.API+"/trabajadores/"

    def maquetador(self, response):
        for valor in response:
            print("-------------------------------------------------------------------------------------")
            print("Id : ", valor['id'])
            print("Nombres : ", valor['nombres'], ": ")
            print("Apellidos: ", valor['apellidos'], ": ")
            print("Cedula: ", valor['cedula'], ": ")
            print("Correo: ", valor['correo'], ": ")
            print("Direccion: ", valor['direccion'], ": ")
            print("Telefono: ", valor['telefono'], ": ")
            print("Area: ", valor['area'], ": ")
            print("Foto: ", valor['foto_trabajador'], ": ")
            print("-------------------------------------------------------------------------------------")
        return response 

    def login(self, correo, cedula):
        response = requests.get(URL)
        seteado = json.loads(response.text)
        for valor in seteado:
            if valor['correo']==correo and valor['cedula']==cedula:
                print('Existe')
                return True
            else:
                print('No Existe')
                return False

       
    def listar(self):
        response = requests.get(URL)
        seteado = json.loads(response.text)
        self.maquetador(seteado)
        

    def buscar(self, id):
        try:
            response = requests.get(URL+str(id))
            seteado = json.loads(response.text)
            # if seteado['cedula']==cedula:
            salida = seteado['nombres']
            print(salida)
            return 
        except:
            print('ID no existen')
            return False

if __name__=='__main__':
    trab = trabajadores()
    # trab.listar()
    trab.buscar(1)
    trab.login('joe.arguello2008@gmail.com', 160100)
