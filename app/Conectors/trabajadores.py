import init
import requests
import json

class trabajadores(init.conexion):
    def __init__(self):
        global URL
        URL = self.API+"/trabajadores/"
        maquetador = init.conexion()

    def login(self, correo, cedula):
        response = requests.get(URL)
        seteado = json.loads(response.text)
        for valor in seteado:
            if valor['correo']==correo and valor['cedula']==cedula and valor['area']=='admin' and valor['area']=='ADMIN':
                print('Admin')
                return 'admin' 
            if valor['correo']==correo and valor['cedula']==cedula:
                print('Existe')
                return True
            else:
                print('No Existe')
                return False

       
    def listar(self):
        response = requests.get(URL)
        seteado = json.loads(response.text)
        self.maquetador.maquetador(seteado)
        
    def buscar(self, id):
        try:
            response = requests.get(URL+str(id))
            seteado = json.loads(response.text)
            # if seteado['cedula']==cedula:
            salida = seteado['nombres']
            print(salida)
            return salida 
        except:
            print('ID no existen')
            return False

    def insertar(self, datos): # Aqui de entrada debe ser un array
        pass

if __name__=='__main__':
    trab = trabajadores()
    trab.listar()
    trab.buscar(1)
    trab.login('jorge.arguello1999@gmail.com', 1600644353)
