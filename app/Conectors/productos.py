import Conectors.init as init
import requests
import json

class productos(init.conexion):
    def __init__(self):
        global URL
        URL = self.API+"/productos/"
        global maquetador
        maquetador = init.conexion()

    def listar(self):
        response = requests.get(URL)
        seteado = json.loads(response.text)
        return maquetador.maquetador_productos(seteado)

    def buscar(self, id):
        try:
            response = requests.get(URL+str(id))
            seteado = json.loads(response.text)
            salida = seteado['nombre']+' '+seteado['precio']
            print(str(salida))
            return salida
        except:
            print('ID no existen')
            return False

    def insertar(self, datos): # Aqui de entrada debe ser un array
        data = dict(
            nombre = datos[0],
            cantidad = datos[1],
            precio = datos[2],
            valor_total = datos[3],
            foto_producto = datos[4],
        )
        try:
            response = requests.post(URL, json=data)
            return True
        except:
            return False

    def editar(self, datos):
        try:
            if self.buscar(id):
                data = dict(
                nombre = datos[0],
                cantidad = datos[1],
                precio = datos[2],
                valor_total = datos[3],
                foto_producto = datos[4],
                )
                response = requests.put(URL+str(id), json=data)
                return True
        except:
            print('No Existe el ID')
            return False

    def eliminar(self, id):
        try:
            if self.buscar(id):
                response = requests.delete(URL+str(id))
                print('Funciona')
                return True
        except:
            print('No Existe el ID')
            return False

if __name__=='__main__':
    prod = productos()
    prod.listar()
    post = ['Coca', 2, 0.50, 1, 1001001]
    prod.insertar(post)
