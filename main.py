from tkinter import ttk
from tkinter import *


class Product:

    def __init__(self, window):
        self.wind= window
        self.wind.title('Cuaderno Notas')

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
        
        #Botones
        ttk.Button(text= 'Comprobar').grid(
                row= 5,
                column= 1,
                sticky= W+E)

    def user(self, window):
        pass

if __name__=='__main__':
    window= Tk()
    aplicacion= Product(window)
    window.mainloop()
 
