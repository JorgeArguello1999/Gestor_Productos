# Gestor de Productos 
 - [¿Que es?](#que-es)
	 - [Forma de Uso](#forma-de-uso)
 - [Instalación](#instalación)
 - [Base de Datos y Docker](../Back-End/README.md)
	 - [Importante](#importante)
	 - [Configuración de Python](#configuración-de-python)
     - [Configuración de JavaScript](#configuración-de-backend)
 - [Errores](#errores)

# ¿Que es?
*/Actualmente esta es la versión 2.2, se han corregido la mayor parte de problemas para crear una base fuerte la cual permita añadir funcionalidades a futuro/*

Una herramienta destinada al manejo de productos y mercancía de forma sencilla y fácil, orientada a personas sin conocimientos en informática. Creada con el principal objetivo de poder utilizarse en casi cualquier dispositivo. 
Teniendo el software en tres presentaciones **GUI**, con la finalidad de poder tener un control amplio de sus productos y mercancía.

## Forma de Uso
**Esta forma de uso esta disponible en caso de que se use desde el código fuente** 
Para usar debemos ejecutar el siguiente comando o archivo: 
> Gestor_Productos.exe

Posteriormente nos pedirá que ingresemos el usuario y contraseña esto se configuro en la INSTALACIÓN por defecto tenemos que esta es "Juan" y la contraseña es "Pilancho".
Teniendo la posibilidad de realizar las siguiente opciones.

  - Manejar Clientes -> Admin
  - Manejar Trabajadores -> Admin
  - Manejar Facturas -> Trabajadores (Cajero)
  - Manejar Productos -> Trabajadores (Bodega)

#### GUI: 
Para usar la Interfaz grafica, primero debe ingresar el usuario en el recuadro requerido, para luego acceder a la parte de administración, esto dependera si tu usuario es Administrador, solo si esto fuera cierto,accederia al menú correspondiente al Administrador.

# Instalacion
## Esto es para Desarrollo
Para la instalación tener en cuenta Docker y Docker compose para crear el servidor
En docker tenemos que Armar la imagen que tenemos en `Back-End`
## Uso en Windows y Linux
Para usar el software tenemos que hacer lo siguiente si tenemos git instalado pero en caso contrario, descargar el [codigo fuente](https://codeload.github.com/JorgeArguello1999/Gestor_Productos/zip/refs/heads/version.2).
```bash
git clone https://github.com/JorgeArguello1999/Gestor_Productos.git
cd Gestor_Productos/app/
python3 splash.py
```
## Importante
Si desea desarrollar o ejecutar las ultimas versiones de *Gestor de Productos*, considere lo siguiente:

Tener instalado **Python3** y **pip3** (Instalador de paquetes de Python3), instalar el conector de Python a **MariaDB** con pip3 para la conexión `pip3 install mariadb` , se esta trabajando con un servidor local, base de datos aplicación, tabla productos y usuarios.
Para desarrollar la GUI necesitas instalar **PyQt5** usando el siguiente comando `pip install PyQt5` depende si lo hacen en Windows, Linux o Mac puede que requiera hacer pasos adicionales.
### Instalación de todo lo necesario para el desarrollo de la aplicación.
Para desarrollar la aplicación usted necesitara disponer de las siguientes aplicaciones en su computador u ordenador:
 - **Base de Datos**
     - **MariaDB** 
     - **SQLite** (Opcional solo para android en caso de no existir un servidor principal)
 - **Conectores y QtDesigner**
     - **mariadb** (Conector de MariaDB con Python)
     - **PyInstaller** (Crear ejecutables de la apliación)
     - **PyQt5** (Conjunto de librearias Qt para desarrollo)
     - **PyQt5-tools** (Herramienta gráfica para desarrollo del entorno gráfico Qt)

Instalación de conectores mediante PIP (Gestor de paquetes de Python)
```bash
pip install mariadb pyqt5 pyqt5-tools
```

Crear ejecutable (Dependiendo el Sistema Operativo compilara un .EXE o un .DMG)
```
pyinstaller --clean --onefile --windowed archivo.py #GUI
```

No termines el título con un punto. Usa mayúsculas al inicio del título y por cada párrafo del cuerpo del mensaje. Usa el modo imperativo en el título. Usa el cuerpo del mensaje para explicar cuáles cambios has hecho y por qué los hiciste. No asumas que las personas que revisará el código entiende cuál era el problema original, asegúrate de agregar la información necesaria. No piense que tu código se explica solo.

## Configuración de Python
Para configurar la conexión con base de datos debemos configurar el archivo `app/Conectors/init.py`, este archivo contiene la configuración para la base de datos, el usuario y las credenciales para acceder a la misma

```python
class conexion:
    API = "http://localhost:3000/api" # Aqui se debe modificar en caso de trabajar con un servidor remoto
    def __init__(self):
        print("Modulo conectado")
```
## Configuración de Backend
En caso de ser necesario tendras que modificar el código del Back-End para esto vamos a modificar el archivo `Back-End/src/database.js` donde se encuentra la configuración de la API

```javascript
const mysql = require('mysql2'); // Aquí puedes modificar en caso de usar otra DBM

const mysqlConnection = mysql.createConnection({
  host: 'localhost', // Dirección de la Base de datos
  user: 'root',// Usuario
  database: 'aplicacion', // Nombre de la Base de datos
  password: 'root', // Contraseña de la Base de datos
  // multipleStatements: true
});
mysqlConnection.connect(function (err) {
  if (err) {
    console.error(err);
    return;
  } else {
    console.log('db is connected');
  }
});
module.exports = mysqlConnection;

```
# Consejos para el desarrollo
## Especifica el tipo de commit 
 - **feat:** La nueva característica que agregas a una aplicación en particular 
 - **fix:** Un parche para un error
 - **style:** Características o actualizaciones relacionadas con estilos
 - **refactor:** Refactorizar una sección específica de la base de código
 - **test:** Todo lo relacionado con pruebas
 - **docs:** Todo lo relacionado con documentación
 - **chore:** Mantenimiento de código regular.

# Errores
## Error (101)
El error 101 en el área de Insertar hace referencia a que en la base de datos ya existe un elemento con el mismo ID, si se quiere registrar un elemento del mismo nombre, se recomienda usar otro ID para evitar este problema
## Error (102)
El error 102 es aquel que aparece cuando se intenta eliminar un producto que no existe en la base de datos.

## Error (103)
El error 103 es aquel que ocurre cuando un elemento a actualizar no existe en la tabla de la base de datos, para solucionarlo debes crear el elemento.

## Error (104)
Este error es producido por la GUI o Interfaz gráfica, este se provoca al ocurrir un error en la inserción de datos en la tabla, debe respetar el tipo de datos que aceptan cada uno Nombre(Texto), ID(Numero Entero), Cantidad (Numero Entero), Precio(Numero Flotante o Decimal).
