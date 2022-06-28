import Conectors.db_connect as db_connect
import sys
import time

# Modulos de Qt5
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit

class interface(QMainWindow):
    user= db_connect.usuarios()
    productos= db_connect.productos()

    def __init__(self):
        super().__init__()
        # Cargamos el XML de Qt
        uic.loadUi("gui/user_gui.ui", self)
        # Deshabilitamos los frames antes del login
        self.frame_Listar.setEnabled(False)
        self.frame_Opciones.setEnabled(False)
        # Modificamos los tamaños de la tabla
        self.tabla_productos.setColumnWidth(0,50)
        self.tabla_productos.setColumnWidth(1,200)
        self.tabla_productos.setColumnWidth(2,70)
        self.tabla_productos.setColumnWidth(3,60)
        # Boton Login
        self.boton_registro.clicked.connect(self.login)

    def cargador_tabla_componentes(self):
        """
        Por cada llamado a la funcion la variable productos almacena nuevos datos
        si la llamamos como propiedad de clase, esta no almacena los nuevos datos.
        """
        productos= db_connect.productos()
        productos= productos.listar()
        fila=0
        self.tabla_productos.setRowCount(len(productos))
        for individual in productos:
            self.tabla_productos.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(individual[0])))
            self.tabla_productos.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(individual[1])))
            self.tabla_productos.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(individual[2])))
            self.tabla_productos.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(individual[3])))
            fila=fila+1
        # Cargamos la seleccion
        self.tabla_productos.cellClicked.connect(self.eleccion_producto)
        # Cargamos boton seleccionar
        self.seleccionar_productos.clicked.connect(self.seleccionar)
        # Cargamos boton de cargar
        self.boton_productos.clicked.connect(self.cargador_tabla_componentes)

    def eleccion_producto(self):
        try:
            global codigoSeleccion
            codigoSeleccion= int(self.tabla_productos.selectedIndexes()[0].data())
            linea= int(self.tabla_productos.currentRow())
            self.tabla_productos.selectRow(linea)
            self.mensaje_productos.setText("")
            print(f"Linea:{linea} ID:{codigoSeleccion}")
            self.seleccionar()
            return codigoSeleccion
        except:
            self.mensaje_productos.setText("[Seleccione el ID del Producto]")

    def menu_opciones(self):
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

    def limpieza(self):
        # Limpiamos los registros
        self.nombre_insertar.setText("")
        self.cantidad_insertar.setText("")
        self.precio_insertar.setText("")
        # Campos Editar
        self.nombreEntrada_editar.setText("")
        self.nombre_editar.setText("")
        self.cantidad_editar.setText(" ")
        self.precio_editar.setText(" ")
        self.id_editar.setText(" ")
        # Campos Eliminar
        self.nombre_eliminar.setText(" ")
        self.id_eliminar.setText(" ")

    """
    Desde aquí comienzan las funciones de los botones
    --> Parte logica
    """
    # Funcion del Boton de Login
    def login(self):
        usuario= self.entrada_usuario.text()
        password= self.entrada_contrasena.text()
        respuesta= self.user.verificador(usuario, password)
        if respuesta==True:
            self.frame_Listar.setEnabled(True)
            self.frame_Opciones.setEnabled(True)
            validacion= "[Autorizado]"
            # Inicamos el componente
            self.cargador_tabla_componentes()
            self.menu_opciones()
            # Llamamos al come procesador
        else:
            validacion= "[No Autorizado]" 
        self.comprobador.setText(validacion)

    # Boton de seleccionar
    def seleccionar(self):
        try: 
            global salida
            salida= self.productos.listar()
            for i in salida:
                if i[0]==codigoSeleccion:
                    codigo=str(i[0])
                    global nombreSeleccion
                    nombreSeleccion=str(i[1])
                    # Mostramos en la opcion de Editar
                    self.id_editar.setText(codigo)
                    self.nombre_editar.setText(nombreSeleccion)
                    # Mostramos en la opcion de Eliminar
                    self.id_eliminar.setText(codigo)
                    self.nombre_eliminar.setText(nombreSeleccion)
                    return nombreSeleccion
        except:
            self.mensaje_productos.setText("[ID no seleccionado]")

    def insertar(self):
        # Obtenemos la entrada del usuario
        try:
            nombre= str(self.nombre_insertar.text())
            cantidad= int(self.cantidad_insertar.text())
            precio= float(self.precio_insertar.text())
            # Evitamos que ingrese algo con el mismo nombre o mismo id
            self.productos.insertar(nombre, cantidad, precio)
            self.cargador_tabla_componentes()
            self.mensaje_insertar.setText("[ Realizado con Exito ]")
        except:
            self.mensaje_insertar.setText("[ Error 104 ]")

    def editar(self):
        try:
            codigo= self.id_editar.text()
            nombre= str(self.nombreEntrada_editar.text())
            cantidad= int(self.cantidad_editar.text())
            precio= float(self.precio_editar.text())
            self.productos.editar(codigo, nombre, cantidad, precio)
            self.mensaje_editar.setText("[Realizado con Exito]")
            self.cargador_tabla_componentes()
        except:
            self.mensaje_editar.setText("[Error 104]")

    def eliminar(self):
        try:
            codigo= self.id_editar.text()
            self.productos.eliminar(codigo)
            self.mensaje_eliminar.setText("[Borrado con Exito]")
            self.cargador_tabla_componentes()
        except:
            self.mensaje_eliminar.setText("[Error ID no seleccionado]")

app= QApplication(sys.argv)
GUI= interface()
GUI.show()
sys.exit(app.exec_())
