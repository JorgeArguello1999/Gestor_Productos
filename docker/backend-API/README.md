# Importante
Para la creacion de la API se han usado los modulos de npm:
 - mysql2
 - morgan
 - nodemon
 - express

# Configuración Basica
En la carpeta `src/` existe un subdirectorio con el nombre `database.js` en el cual se debera configurar tanto el usuario al igual que la IP del servidor, o donde este corriendo el contenedor de Docker
> Se planea integrar todo en un solo contenedor de Docker para eliminar este paso.

```javascript
const mysql = require('mysql2');

const mysqlConnection = mysql.createConnection({
  host: '192.168.1.13', // Direccion IP del servidor
  user: 'root', // Usuario de la base de datos
  database: 'aplicacion', //base de datos
  password: 'root', // Contraseña
  // port: 3306, // En caso de tener otro puerto para MySQL
});
```

# Uso
Para conectarse a la API debe completar todos los requerimientos, solo el `id`en las tablas no es necesario llenarlo, ya que este lo hace de forma automatica, para mas información del tipo de información y datos que acepta cada campo y cada tabla visite la documentación de [docker](../docker/README.md) para obtener más detalles.

> Considerando a futuro mejorar, al contrario de tener miles de rutas para cada tabla, crear un `proceso almacenado` de SQL con el cual solo se tendría que especificar que tipo de acción se quiere realizar y que datos del usuario necesito, así ahorraria codigo y lo haría más fácil a la hora, de añadir funcionalidades y mantener el código, solo que aumentaria la complejidad.
## Trabajadores (Ejemplo)
```json
{
    "id":1, //Este valor es opcional en caso que se trabaje con un PUT o un POST
    "nombres":"Jorge Alexander",
    "apellidos":"Arguello Gusqui",
    "cedula":1600644353,
    "correo":"jorge.arguello1999@gmail.com",
    "direccion":"Dorado",
    "telefono":989402524,
    "area":"admin",
    "foto_trabajador":null //Aqui se coloca una fotografia
    }
```