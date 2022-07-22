import Conectors.trabajadores as trabajadores
import Conectors.productos as productos

login = trabajadores.trabajadores()
produ = productos.productos()
# correo = input('Insgresa tu correo: ')
# cedula = int(input('Ingresa tu cedula: '))
correo = str('juanpilancho@gmail.com')
cedula = int(160100)
if correo!=None and cedula !=None:
    produ.listar()
    if login.login(correo, cedula):
        import gui.user_gui
else:
    exit()
