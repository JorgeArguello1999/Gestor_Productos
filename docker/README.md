# Docker 
Así funciona el script para Docker
```bash
#!/bin/bash

echo "Elije el Gestor de Base de Datos que desees usar: "
echo "MariaDB: 1"
echo "MySQL: 2"
read -p "Elección: " eleccion

docker run --name phpmyadmin -d -e PMA_HOST=192.168.1.13 -p 8080:80 phpmyadmin
echo "phpmyadmin corriendo en el puerto 8080"

if [[ $eleccion -eq 1 ]]
then
	echo "MariaDB"
	# MariaDB
	docker run -v ~/personal/Gestor_Productos/basededatos/docker_Mariadb_DB:/var/lib/mysql -p 3306:3306 --name gestor_productos --env MARIADB_USER=jorge --env MARIADB_PASSWORD=basededatos -d --env MARIADB_ROOT_PASSWORD=root mariadb

	# EXEC
	docker exec -it gestor_productos mysql -u jorge -p

else
	echo "MySQL"
	# MySQL
	docker run -v ~/personal/Gestor_Productos/basededatos/docker_MySQL_DB:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 --name gestor_productos -d mysql

	# EXEC
	docker exec -it gestor_productos mysql -u root -p

fi

echo "------------------------------------------------------------------------"

```

# Base de Datos
Para la creación de la base de datos primero tenemos que crear la base de datos, siguiendo estos pasos:

## Base de Datos
```sql
CREATE DATABASE aplicacion;
USE aplicacion;
``` 

## Productos
```sql
CREATE TABLE productos( 
    id INTEGER(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30), 
    cantidad INTEGER(11), 
    precio FLOAT,
    valor_total FLOAT,
    foto_producto BLOB)
    ENGINE= 'InnoDB' DEFAULT CHAR SET= latin1;
```

```text
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| id            | int(11)     | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(30) | YES  |     | NULL    |                |
| cantidad      | int(11)     | YES  |     | NULL    |                |
| precio        | float       | YES  |     | NULL    |                |
| valor_total   | float       | YES  |     | NULL    |                |
| foto_producto | blob        | YES  |     | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
```
## Clientes
```sql
CREATE TABLE clientes( 
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nombres VARCHAR(20) NOT NULL, 
    apellidos VARCHAR(20) NOT NULL, 
    cedula INT NOT NULL,
    correo VARCHAR(50) NOT NULL,
    direccion VARCHAR(20)NOT NULL,
    telefono INT NOT NULL) 
    ENGINE= 'InnoDB' DEFAULT CHAR SET= latin1;
```

```text
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| nombres   | varchar(20) | NO   |     | NULL    |                |
| apellidos | varchar(20) | NO   |     | NULL    |                |
| cedula    | int(11)     | NO   |     | NULL    |                |
| correo    | varchar(50) | NO   |     | NULL    |                |
| direccion | varchar(20) | NO   |     | NULL    |                |
| telefono  | int(11)     | NO   |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```

## Trabajadores
```sql
CREATE TABLE trabajadores( 
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nombres VARCHAR(20) NOT NULL, 
    apellidos VARCHAR(20) NOT NULL, 
    cedula INT NOT NULL,
    correo VARCHAR(50) NOT NULL,
    direccion VARCHAR(20)NOT NULL,
    telefono INT NOT NULL,
    area VARCHAR(20) NOT NULL,
    foto_trabajador BLOB) 
    ENGINE= 'InnoDB' DEFAULT CHAR SET= latin1;
```

```text
+-----------------+-------------+------+-----+---------+----------------+
| Field           | Type        | Null | Key | Default | Extra          |
+-----------------+-------------+------+-----+---------+----------------+
| id              | int(11)     | NO   | PRI | NULL    | auto_increment |
| nombres         | varchar(20) | NO   |     | NULL    |                |
| apellidos       | varchar(20) | NO   |     | NULL    |                |
| cedula          | int(11)     | NO   |     | NULL    |                |
| correo          | varchar(50) | NO   |     | NULL    |                |
| direccion       | varchar(20) | NO   |     | NULL    |                |
| telefono        | int(11)     | NO   |     | NULL    |                |
| area            | varchar(20) | NO   |     | NULL    |                |
| foto_trabajador | blob        | YES  |     | NULL    |                |
+-----------------+-------------+------+-----+---------+----------------+
```

## Factura
```sql
CREATE TABLE factura( 
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    cliente VARCHAR(20) NOT NULL, 
    fecha INT,
    ciudad VARCHAR(20) NOT NULL, 
    compras BLOB,
    subtotal FLOAT,
    descuento FLOAT,
    iva FLOAT,
    total FLOAT) 
    ENGINE= 'InnoDB' DEFAULT CHAR SET= latin1;
```

```text
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| cliente   | varchar(20) | NO   |     | NULL    |                |
| fecha     | int(11)     | YES  |     | NULL    |                |
| ciudad    | varchar(20) | YES  |     | NULL    |                |
| compras   | blob        | YES  |     | NULL    |                |
| subtotal  | float       | YES  |     | NULL    |                |
| descuento | float       | YES  |     | NULL    |                |
| iva       | float       | YES  |     | NULL    |                |
| total     | float       | YES  |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```
