import db_connect
import tkinter
from tkinter import ttk
from tkinter import *

class Producto:
    def __init__(self, window):
        self.wind= window
        self.wind.title('Sistema de Registro')

        #Creamos un Frame
        frame= LabelFrame(self.wind, text='Datos')
        frame.grid(
                row= 0,
                column= 0,
                columnspan= 3,
                pady= 20)

        #Entrada de Nombre
        Label(frame, text='Nombre: ').grid(
                row= 1,
                column= 0)
        self.name= Entry(frame)
        self.name.focus()
        self.name.grid(
                row= 1,
                column= 1)

        #Entrada de Contraseña 
        Label(frame, text='Contraseña: ').grid(
                row= 2,
                column= 0)
        self.name= Entry(frame)
        self.name.grid(
                row= 2,
                column= 1)

        #Comprobar datos
        ttk.Button(frame, text='Registro', command=self.wind.destroy ).grid(
                row= 3,
                columnspan= 2,
                sticky= W+E)


        #Boton de Salir
        ttk.Button(frame, text='Salir', command=self.wind.destroy ).grid(
                row= 4,
                columnspan= 2,
                sticky= W+E)

        def comprobador():
            pass

if __name__=='__main__':
    window= Tk()
    aplicacion= Producto(window)
    window.mainloop()
 
