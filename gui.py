import db_connect
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit

class ejemplo_Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz_grafica.ui", self)

        # Boton Login
        self.boton_registro.clicked.connect(self.login)


    def login(self):
        # Llamamos a la funcion de verificacion de la Base de 
        con=db_connect.conexion()

        user= self.entrada_usuario.text()
        password= self.entrada_contrasena.text()
        respuesta= con.verificador(user, password)

        if respuesta==True:
            validacion="[ Autorizado ]"
        else:
            validacion="[ No Autorizado ]"

        self.comprobador.setText(validacion)


if __name__=="__main__":
    app= QApplication(sys.argv)
    GUI= ejemplo_Gui()
    GUI.show()
    sys.exit(app.exec_())
