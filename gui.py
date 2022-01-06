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
        self.tabla_productos.setColumnWidth(0,50)
        self.tabla_productos.setColumnWidth(1,200)
        self.tabla_productos.setColumnWidth(2,70)
        self.tabla_productos.setColumnWidth(3,60)

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

        #self.tabla_productos.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tabla_productos.cellClicked.connect(self.retornador)
        #self.tabla_productos.itemSelectionChanged.connect(self.retornador)
        
        # Funcion del boton Recargar
        self.boton_productos.clicked.connect(self.cargador)

    def retornador(self):
        try:
            codigo= int(self.tabla_productos.selectedIndexes()[0].data())
            linea= int(self.tabla_productos.currentRow())
            self.tabla_productos.selectRow(linea)
            print("Linea:", linea, "\nID:", codigo)
            self.mensaje_productos.setText(" ")

            return codigo
        except:
            self.mensaje_productos.setText("[ Seleccione el ID del producto ]")

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
        try:
            # Obtenemos la entrada del usuario
            codigo= int(self.id_insertar.text())
            nombre= str(self.nombre_insertar.text())
            cantidad= int(self.cantidad_insertar.text())
            precio= float(self.precio_insertar.text())

            if self.pro.detector(codigo, nombre)!=True:
                # Evitamos que ingrese algo con el mismo nombre o mismo id
                # Llamamos a la funcion del componente db_connect.insertar 
                self.pro.insertar(codigo, nombre, cantidad, precio)
                # Insertamos el cargador para ver lo añadido
                self.cargador()
                self.mensaje_insertar.setText("[ Realizado con Exito ]")
        except:
            self.mensaje_insertar.setText("[ Error 104 ]")

    def editar(self):
        """
        Lo que esta pasando es que se queda en el retornador y no avanza de ahi
        codigo= self.retornador()
        print(type(codigo))
        self.nombre_editar.setText(codigo)
        """
        pass

    def eliminar(self):
        pass

if __name__=="__main__":
    app= QApplication(sys.argv)
    GUI= ejemplo_Gui()
    GUI.show()
    sys.exit(app.exec_())
