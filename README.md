# Manegador de Productos 
## ¿Que es?
Una herramienta para el manego de productos puede ser en un local de comida, ropa o cualquier tipo de negocio interesado en tener un control de todos los productos en almacen

# Instalacion
## Importante
Tener instalado python3 y pip3 (Instalador de paquetes de python3), instalar mariadb con pip3 para la conexion, se esta trabajando con un servidor local, base de datos aplicacion, tabla productos y usuarios
## Creacion de la Base de datos
Para crear la Base de datos necesitaremos MariaDB o en su defecto MySQL 4.04 en adelante. Esto se recomienda ya que se usa el cifrado AES que esta disponible desde la version 4.04 en adelante en el gestor de Base de Datos MySQL y MariaDB, digite los siguientes comandos dentro de la consola de MySQL o MariaDB
https://www.youtube.com/watch?v=Cei5rzFjYgM

## Configuracion
Para configurar la conexion con base de datos debemos configurar el archivo db_connect, ahi se coloca la configuracion para la base de datos, el usuario y las credenciales para acceder a la misma

# Uso
## CLI
Para usar el cli debemos ejecutar el comando 
` python3 cli.py `
Posteriormente nos pedira que ingresemos el usuario y contraseña esto se configuro en la INSTALACION por defecto tenemos que esta es "Georgi" y la contraseña es "contrasena"

## Configuración de la Base de Datos
Base de datos= "aplicacion"
Tablas:
- productos
    - id (int 11)
    - nombre (varchar 30)
    - cantidad (init 11)
    - precio (float)

- usuarios
    - nombre (varchar 30)
    - clave (varchar 10)

# Errores
## Error (101)
El error 101 en el area de Insertar hace referencia a que en la base de datos ya existe un elemento con el mismo ID, si se quiere registrar un elemento del mismo nombre, se recomienda usar otro ID para evitar este problema
## Error (102)
El error 102 es aquel que aparece cuando se intenta eliminar un producto que no existe en la base de datos.

## Error (103)
El error 103 es aquel que ocurre cuando un elemento a actualizar no existe en la tabla de la base de datos, para solucionarlo debes crear el elemento.
