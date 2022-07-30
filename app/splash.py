# Modulo Tkinter
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as MessageBox

# Modulo del Sistema
import sys

# Modulo de Conexion
import Conectors.trabajadores as trabajadores

class splash:
    root = Tk()
    def createGUI(self):
        # Titulo
        self.root.title("Login Usuario")

        # mainFrame
        mainFrame = Frame(self.root)
        mainFrame.pack()
        mainFrame.config(width=480,height=320)#,bg="lightblue")

        # textos y titulos
        titulo = Label(mainFrame,text="Gestor de Productos",font=("Arial",24))
        titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)

        nombreLabel = Label(mainFrame,text="Correo: ")
        nombreLabel.grid(column=0,row=1)
        passLabel = Label(mainFrame,text="Contraseña: ")
        passLabel.grid(column=0,row=2)

        # entradas de texto
        self.usuario = StringVar()
        nombreEntry = Entry(mainFrame, textvariable=self.usuario)
        nombreEntry.grid(column=1,row=1)

        self.password = StringVar()
        contraEntry = Entry(mainFrame,textvariable=self.password, show="*")
        contraEntry.grid(column=1,row=2)

        # botones
        iniciarSesionButton = ttk.Button(mainFrame,text="Iniciar Sesion", command=self.iniciarSesion)
        iniciarSesionButton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

        # Iniciamos el mainloop
        self.root.mainloop()

    def iniciarSesion(self):
        # Llamamos al modulo
        trabajador = trabajadores.trabajadores()
        respuesta =  trabajador.login(self.usuario.get(), self.password.get())
        # Admin
        if respuesta=='admin':
            print(respuesta)
            return 'admin' and exit()
        # Trabajador
        if respuesta:
            print(respuesta)
            import gui.user_gui
            exit()
        else:
            print(respuesta)
            exit()

if __name__=="__main__":
    app = splash()
    app.createGUI()
    user= 'joe.arguello2008@gmail.com'
    password = int(1600611)
