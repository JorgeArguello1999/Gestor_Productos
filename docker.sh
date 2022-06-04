#!/bin/bash

echo "Elije el Gestor de Base de Datos que desees usar: "
echo "MariaDB: 1"
echo "MySQL: 2"
read -p "Elección: " eleccion

echo "------------------------------------------------------------------------"

echo "La contraseña root se ha establecido por defecto"
read -p "Ingrese el nombre del usuario DB: " usuario
read -sp "Ingrese contraseña para el usuario: " password

echo "------------------------------------------------------------------------"

if [[ $eleccion -eq 1 ]]
then
	echo "MariaDB"
	docker run --detach -p 3306:3306 --name gestor_productos --env MARIADB_USER=$usuario --env MARIADB_PASSWORD=$password --env MARIADB_ROOT_PASSWORD=root mariadb:latest 
	docker exec -it gestor_productos mysql -u $usuario -p 
else
	echo "MySQL"
	docker run -v ~/personal/Gestor_Productos/docker_DB:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 --name gestor_productos -d mysql
	docker exec -it gestor_productos mysql -u root -p
fi

echo "------------------------------------------------------------------------"

