# Gestor de Productos
![Logo de la Aplicación](Images/logo.png)

 - [Instalación y uso](#instalación-y-uso)
 - [Documentación APP](./app/README.md)
 - [Documentación Back-End](./Back-End/README.md)

Aplicación de Gestión de Producto para el negocio. Para poder facilitar el manejo de los productos con la finalidad de tener todo organizado y registrado en un sistema digital.

Esto se pospone hasta terminar el proyecto, la demas documentación se encuentra dentro de cada zona: Back-End y App 

## Instalación y uso:
Para utilizar el programa debemos descargar la aplicación:
```bash
git clone https://github.com/JorgeArguello1999/Cuaderno_Notas.git
```
> También puedes descargar el código comprimido [Archivo comprimido en formato .zip](https://github.com/JorgeArguello1999/Gestor_Productos/archive/refs/heads/version.2.2.zip) 

Despues ingresamos al directorio `Back-End` y ejecutamos docker-compose para crear una imagen para la **API** 
```bash
./Back-End/ # Ruta donde debe estar el Dockerfile
docker build -t prueba:1 .
``` 
También puedes crear la base de datos desde el docker-compose pero en caso contrario ejecutar el siguiente comando:
```bash
docker run -v ~/personal/data/docker_Mariadb_DB:/var/lib/mysql -p 3306:3306 --name gestor_productos --env MARIADB_USER=jorge --env MARIADB_PASSWORD=basededatos -d --env MARIADB_ROOT_PASSWORD=root mariadb
```
En caso de que no quieras crear la Imagen puedes correr la API desde la carpeta del Back-End
```bash
node index.js
```

## Login/Splash
Esta es la pantalla de bienvenida, esta realizada en Tkinter.
1. Ingresas tu correo
2. Ingresas tu cédula -> Esto es solo temporal
![Login/Splash](Images/GPgui1.png)
## Pantalla de Trabajador (Cajero && Bodega)
Obtenemos la pantalla para manejar los productos, en futuras versiones existira mayor funcionalidad.
![Login/Splash](Images/GPgui2.png)