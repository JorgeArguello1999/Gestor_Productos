class conexion:
    API = "http://localhost:3000/api" # Aqui se debe modificar en caso de trabajar con un servidor remoto

    def __init__(self):
        print("Modulo conectado")

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

    def maquetador_productos(self, response):
        for valor in response:
            print("-------------------------------------------------------------------------------------")
            print("Id : ", valor['id'])
            print("Nombre : ", valor['nombre'], ": ")
            print("Cantidad : ", valor['cantidad'], ": ")
            print("Precio : ", valor['precio'], ": ")
            print("Valor : ", valor['valor_total'], ": ")
            print("Foto : ", valor['foto_producto'], ": ")
            print("-------------------------------------------------------------------------------------")
        return response



