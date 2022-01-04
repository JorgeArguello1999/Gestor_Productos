import db_connect
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit

class ejemplo_Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz_grafica.ui", self)

        # Boton Login
        self.boton_registro.clicked.connect(self.login)


    def login(self):
        # Llamamos a la funcion de verificacion de la Base de 
        self.con=db_connect.conexion()

        user= self.entrada_usuario.text()
        password= self.entrada_contrasena.text()
        respuesta= self.con.verificador(user, password)

        if respuesta==True:
            validacion="[ Autorizado ]"
            # Iniciamos el cargador para la tabla
        else:
            validacion="[ No Autorizado ]"

        self.comprobador.setText(validacion)
        self.cargador()

    def cargador(self):
        self.pro= db_connect.productos()
        datos= self.pro.listar()
        row=0
        for producto in datos:
            self.tabla_productos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(producto[0])))
            self.tabla_productos.setItem(row, 1, QtWidgets.QTableWidgetItem(producto[1]))
            self.tabla_productos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(producto[2])))
            self.tabla_productos.setItem(row, 3, QtWidgets.QTableWidgetItem(str(producto[3])))
            row= row+1

if __name__=="__main__":
    app= QApplication(sys.argv)
    GUI= ejemplo_Gui()
    GUI.show()
    sys.exit(app.exec_())
