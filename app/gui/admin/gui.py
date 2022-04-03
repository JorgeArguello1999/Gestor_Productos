import sys
# Establecemos un path de python para la estructura de paquetes
import Conectors.db_connect as db_connect
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit

class admin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/admin/normal_user.ui", self)

    def arranque(self, usuario, password):
        # Deshabilitamos los frames 
        self.frame_Listar.setEnabled(False)
        self.frame_Opciones.setEnabled(False)
        
        # Modificamos los tamaños de la tabla
        self.tabla_productos.setColumnWidth(0,50)
        self.tabla_productos.setColumnWidth(1,200)
        self.tabla_productos.setColumnWidth(2,70)
        self.tabla_productos.setColumnWidth(3,60)

        print(usuario, password)

        # Boton Login
        self.boton_registro.clicked.connect(self.login)

    def login(self):
        print("Holis")



# Ejecutamos la aplicacion
if __name__=="__main__":
    app= QApplication(sys.argv)
    GUI= admin()
    GUI.show()
    sys.exit(app.exec_())
