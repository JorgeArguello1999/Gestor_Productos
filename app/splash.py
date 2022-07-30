# Modulo del Sistema
import sys

# Modulo de Conexion
import Conectors.trabajadores as trabajadores 

# Modulos de Qt5
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit

class splash(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('splash.ui', self)
        self.ingresar.clicked.connect(self.login)

    def login(self):
        trabajador = trabajadores.trabajadores()
        user = str(self.user.text())
        password = int(self.password.text()) # Por el momento es la cedula

        print(user, password)
        print(type(user), type(password))

        if trabajador.login(user, password)=='admin':
            print('admin')
            # import gui.user_gui

        if trabajador.login(user, password):
            # import gui.user_gui
            print('trabajador')
        else:
            print('ni idea')
            exit()

if __name__=='__main__':
    app= QApplication(sys.argv)
    GUI= splash()
    GUI.show()
    sys.exit(app.exec_())
