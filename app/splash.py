"""
import gui.admin.gui as admin
typeuser= admin.admin()
typeuser.arranque("Jorge", "contrasena")
if True:
    import gui.user_gui  
else:
    print("No vale :c ")
"""
import Conectors.trabajadores as trabajadores

login = trabajadores.trabajadores()

correo = input('Insgresa tu correo: ')
cedula = int(input('Ingresa tu cedula: '))

if correo!=None and cedula !=None:
    if login.login(correo, cedula):
        import gui.user_gui
else:
    exit()
