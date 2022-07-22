import Conectors.init as init
import requests
import json

class trabajadores(init.conexion):
    def __init__(self):
        global URL
        URL = self.API+"/trabajadores/"
        global maquetador
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
        maquetador.maquetador(seteado)
        return True

    def buscar(self, id):
        try:
            response = requests.get(URL+str(id))
            seteado = json.loads(response.text)
            salida = seteado['nombres']+' '+seteado['apellidos']
            print(str(salida))
            return salida 
        except:
            print('ID no existen')
            return False

    def insertar(self, datos): # Aqui de entrada debe ser un array
        data = dict(
            nombres = datos[0], 
            apellidos = datos[1],
            cedula = datos[2],
            correo = datos[3],
            direccion = datos[4],
            telefono = datos[5],
            area = datos[6], #(admin, cajero, bodega)
            foto = datos[7] #(Imagen JPG o PNG)
        )
        try:
            response = requests.post(URL, json=data)
            return True
        except:
            return False

    def editar(self, id, datos):
        try:
            if self.buscar(id):
                data = dict(
                    nombres = datos[0], 
                    apellidos = datos[1],
                    cedula = datos[2],
                    correo = datos[3],
                    direccion = datos[4],
                    telefono = datos[5],
                    area = datos[6], #(admin, cajero, bodega)
                    foto = datos[7] #(Imagen JPG o PNG)
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
    trab = trabajadores()
    trab.listar()
    # trab.buscar(1)
    # trab.login('jorge.arguello1999@gmail.com', 1600644353)
    # post = ['Juan Andres', 'Pilancho Paredes', 160100, 'juanpilancho@gmail.com', 'Shell', 987578898, 'bodega', 110]
    # trab.insertar(post)
    # trab.eliminar(1)
