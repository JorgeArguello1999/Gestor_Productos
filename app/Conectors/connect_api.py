import requests
import json

class conexion:
    API = "http://localhost:3000/api" # Aqui se debe modificar en caso de trabajar con un servidor remoto

    def __init__(self):
        print("Modulo conectado")

class trabajadores(conexion):
    def listar(self):
        response = requests.get(self.API+"/trabajadores/")
        response = response.json()

        '''
        for i in response:
            print(i, ":", response[i], '\n')
        '''

        for i in response:
            print(response)

if __name__=='__main__':
    tra= trabajadores()
    tra.listar()
