# Gestor de Productos 
## ¿Que es?
Una herramienta para el manejo de productos puede ser en un local de comida, ropa o cualquier tipo de negocio interesado en tener un control de todos los productos en almacén

# Instalación
## Importante
Tener instalado python3 y pip3 (Instalador de paquetes de python3), instalar MariaDB con pip3 para la conexión, se esta trabajando con un servidor local, base de datos aplicación, tabla productos y usuarios.
Para desarrollar la GUI necesitas instalar PyQt5
## Creación de la Base de datos
Para crear la Base de datos necesitaremos MariaDB o en su defecto MySQL 4.04 en adelante. Esto se recomienda ya que se usa el cifrado AES que esta disponible desde la versión 4.04 en adelante en el gestor de Base de Datos MySQL y MariaDB, ingrese los siguientes comandos dentro de la consola de MySQL o MariaDB

### Creación de la Base de Datos
```
create database aplicacion;
use aplicacion;
```

### Creación de la Tabla para los usuarios
```
create table usuarios( id_usuario integer not null, usuario varchar(20) not null, clave varchar(50) not null ) engine= 'InnoDB' default char set= latin1;
```

### Creación de la Tabla para los productos
```
create table productos( id integer(11), nombre varchar(30), cantidad integer(11), precio float);
```
## Esquema de la Base de Datos
Base de datos= "aplicacion"
Tablas:
- productos
    - id (int 11)
    - nombre (varchar 30)
    - cantidad (init 11)
    - precio (float)

- usuarios
    - id_usuario (int not null) 
    - usuario (varchar 20 not null) 
    - clave (varchar 50 not null) 
## Configuración
Para configurar la conexión con base de datos debemos configurar el archivo `db_connect.py`, este archivo contiene la configuración para la base de datos, el usuario y las credenciales para acceder a la misma
```
import mariadb #Este es el modulo de conexión (MariaDB)

class conexion:
    #Verificacion de usuario
    def __init__(self):
        self.conn = mariadb.connect(
            user="root", #Aqui colocamos el usuario para la base de datos
            password="", #Contraseña para la misma
            host="localhost", #El lugar de la base de datos localhost=127.0.0.1 o alguna otra.
            database="aplicacion" #Nombre de la base de Datos a usar.
            )
```
# Uso
## CLI 
Para usar el CLI debemos ejecutar el comando ` python3 cli.py ` Posteriormente nos pedirá que ingresemos el usuario y contraseña esto se configuro en la INSTALACIÓN por defecto tenemos que esta es "Juan" y la contraseña es "Pilancho"




# Errores

## Error (101)
El error 101 en el área de Insertar hace referencia a que en la base de datos ya existe un elemento con el mismo ID, si se quiere registrar un elemento del mismo nombre, se recomienda usar otro ID para evitar este problema
## Error (102)
El error 102 es aquel que aparece cuando se intenta eliminar un producto que no existe en la base de datos.

## Error (103)
El error 103 es aquel que ocurre cuando un elemento a actualizar no existe en la tabla de la base de datos, para solucionarlo debes crear el elemento.

## Error (104)
Este error es producido por la GUI o Interfaz gráfica, este se provoca al ocurrir un error en la inserción de datos en la tabla, debe respetar el tipo de datos que aceptan cada uno Nombre(Texto), ID(Numero Entero), Cantidad (Numero Entero), Precio(Numero Flotante o Decimal).
