#!/bin/bash

echo "Elije el Gestor de Base de Datos que desees usar: "
echo "MariaDB: 1"
echo "MySQL: 2"
read -p "Elección: " eleccion

if [[ $eleccion -eq 1 ]]
then
	echo "MariaDB"
	# MariaDB
	docker run -v ~/personal/Gestor_Productos/basededatos/docker_Mariadb_DB:/var/lib/mysql -p 3306:3306 --name gestor_productos --env MARIADB_USER=jorge --env MARIADB_PASSWORD=basededatos -d --env MARIADB_ROOT_PASSWORD=root mariadb

	# EXEC
	docker exec -it gestor_productos mysql -u root -p

else
	echo "MySQL"
	# MySQL
	docker run -v ~/personal/Gestor_Productos/basededatos/docker_MySQL_DB:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 --name gestor_productos -d mysql

	# EXEC
	docker exec -it gestor_productos mysql -u root -p

fi

echo "------------------------------------------------------------------------"

