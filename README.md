# PBD - Python-DB-Api
La Python DB API es un conjunto de clases y funciones comunes y estandarizadas para los distintos motores de bases de datos o wrappers de estos escritos en Python. La DB-API está diseñada para ser relativamente independiente de detalles especificos de un motor de bases de datos, permitiendo escribir código de acceso a bases de datos portable entre distintos motores.

REQUISITOS PREVIOS.
Python. https://www.python.org/downloads/ 
DBMS MariaDB o MySQL, https://mariadb.com/kb/en/library/getting-installing-and-upgrading-mariadb/ o https://dev.mysql.com/downloads/installer/, y el motor de bases de datos embebidadas SQLite, https://sqlite.org/download.html.
Interfaz de Python para bases de datos Mysql (https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip) y SQLite (incluido en la python standa). 
Es necesario crear un usuario en la base de datos con nombre ''
Crear la base de datos de Sectores y Personas. Hay un script con las consultas necesarias para su creación que está disponible en el fichero 'create_db_queries.sql' (son las mismas para MariaDB y para SQLite).
Alternativas para la instalación: https://www.linuxbabe.com/linux-server/install-apache-mariadb-and-php7-lamp-stack-on-ubuntu-16-04-lts
Extra: para instalar db.py, $sudo pip3 install db

EJEMPLOS DISPONIBLES EN EL REPOSITORIO.
1. mysql_sample.py --Ejemplo de CRUD y de creación y destrucción de las tablas Personas y Sectores.
2. sqlite_sample.py --Ejemplo de CRUD y de creación y destrucción de la base de datos embebida.
3. demo_select.py -- Ejemplo de selección
4. demo_insert.py -- Ejemplo de inserciones a través de un script
5. demo_update.py -- Ejemplo de actualización
6. demo_delete.py -- Ejemplo de inserción
7. create_db_queries.sql -- Script para la creacin de la base de datos
8. insert_script.sql -- Script con sentencias de inserción
8. SQLiteDB.py -- Ejemplo con db.py
9. dbmanager.py -- Clase para acceso a bases de datos mysql con db.py
10. dbpy_mariadb.py -- Ejemplos con la clase dbmanager.py
11. sqlite_sample.ipynb -- Notebook con ejemplo de python DB API y SQLite
12. oracle_sample.py -- Ejemplo de conexión con DBMS Oracle
