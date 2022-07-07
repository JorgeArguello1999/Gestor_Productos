import requests
import json

class conexion:
    API = "http://localhost:3000/api" # Aqui se debe modificar en caso de trabajar con un servidor remoto

    def __init__(self):
        print("Modulo conectado")

class trabajadores(conexion):
    def listar(self):
        response = requests.get(self.API+"/trabajadores/")
        # No tocar, funcion y eso es lo importante
        seteado = json.loads(response.text)
        print(seteado)

    def buscar(self, id):
        id = str(id)
        response = requests.get(self.API+"/trabajadores/"+id)
        seteado = json.loads(response.text)
        print(seteado)



if __name__=='__main__':
    tra= trabajadores()
    # tra.listar()
    tra.buscar(3)
