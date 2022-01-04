import db_connect
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit

class ejemplo_Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz_grafica.ui", self)
        # Deshabilitamos los frames 
        self.frame_Listar.setEnabled(False)
        self.frame_Opciones.setEnabled(False)
        
        # Modificamos los tamaños de la tabla
        self.tabla_productos.setColumnWidth(0,40)
        self.tabla_productos.setColumnWidth(1,190)
        self.tabla_productos.setColumnWidth(2,70)
        self.tabla_productos.setColumnWidth(2,60)

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
            # Habilitamos los frames
            self.frame_Listar.setEnabled(True)
            self.frame_Opciones.setEnabled(True)
            # Iniciamos el cargador para la tabla
            self.cargador()
            # Iniciamos las opciones
            self.opciones()

        else:
            validacion="[ No Autorizado ]"

        self.comprobador.setText(validacion)

    # Cargamos los datos de la tabla
    def cargador(self):
        self.pro= db_connect.productos()
        datos= self.pro.listar()
        row=0
        self.tabla_productos.setRowCount(len(datos))
        for producto in datos:
            self.tabla_productos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(producto[0])))
            self.tabla_productos.setItem(row, 1, QtWidgets.QTableWidgetItem(str(producto[1])))
            self.tabla_productos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(producto[2])))
            self.tabla_productos.setItem(row, 3, QtWidgets.QTableWidgetItem(str(producto[3])))
            row=row+1

        salida= self.tabla_productos.selectedItems()
        for i in salida:
            print(i)

    # Iniciamos las opciones para la tabla
    def opciones(self):
        # Deshabilitamos los campos de Nombre e ID para las opciones de Editar y Eliminar
        self.id_editar.setEnabled(False)
        self.nombre_editar.setEnabled(False)
        self.id_eliminar.setEnabled(False)
        self.nombre_eliminar.setEnabled(False)

        # Boton para insertar elementos
        self.boton_insertar.clicked.connect(self.insertar)
        # Boton para Editar elementos
        self.boton_editar.clicked.connect(self.editar)
        # Boton para Eliminar elementos
        self.boton_eliminar.clicked.connect(self.eliminar)

    def insertar(self):
        codigo= self.id_insertar.text()
        nombre= self.nombre_insertar.text()
        cantidad= self.cantidad_insertar.text()
        precio= self.precio_insertar.text()

        if self.pro.insertar(codigo, nombre, cantidad, precio)==True:
            validacion= "[ Realizado con Exito ]"
        else:
            validacion= "[ Error 104 ]"

        self.mensaje_insertar.setText(validacion)    

    def editar(self):
        pass

    def eliminar(self):
        pass

if __name__=="__main__":
    app= QApplication(sys.argv)
    GUI= ejemplo_Gui()
    GUI.show()
    sys.exit(app.exec_())
