/*Crear la base de datos y acceder a ella*/
CREATE DATABASE pbd_sample;
USE pbd_sam ple;

/*Crear las tablas*/
CREATE TABLE sectores (
  codS INT,
  nombreS VARCHAR(20),
  porcentS INT,
  ingresosS INT,
  PRIMARY KEY (codS)
);

CREATE TABLE poblacion (
  dni VARCHAR(9),
  nombre VARCHAR(12),
  apellido1 VARCHAR(12),
  apellido2 VARCHAR(12),
  fechanac DATE,
  direccion VARCHAR(20),
  cp VARCHAR(5),
  sexo VARCHAR(1),
  ingresos INT,
  gastosFijos INT,
  gastosAlim INT,
  gastosRopa INT,
  sector INT,
  PRIMARY KEY (dni),
  FOREIGN KEY (sector)
  REFERENCES sectores (codS)
    ON DELETE SET NULL
);

/*Insertar tuplas de ejemplo*/
INSERT INTO sectores
  VALUES (1,'Agricultura y pesca',0,0);

INSERT INTO sectores
  VALUES (2,'Industria y energía',0,0);

INSERT INTO sectores
  VALUES (3,'Servicios',0,0);

INSERT INTO sectores
  VALUES (4,'Construcción',0,0);

INSERT INTO poblacion
  VALUES ('123456789','Carlos','Gutiérrez','Pérez','15/11/1997','Pz. Colón','06300','H',15000,4000,4000,3000,1);

INSERT INTO poblacion
  VALUES ('777888999','Gerardo','Martín','Duque','12/12/1961','C. del Atún','06002','H',23000,6000,5000,4000,1);

INSERT INTO poblacion
  VALUES ('222333444','Pedro','Sánchez','González','01/02/1960','C. Ancha','06300','H',22000,5000,3000,2000,1);

INSERT INTO poblacion
  VALUES ('333444555','María','García','Gil','10/04/1971','C. Diagonal','06400','M',19500,3000,3000,3000,1);

INSERT INTO poblacion
  VALUES ('666884444','Ignacio','Costa','Burgos','12/12/1982','C. Descubrimiento','10005','H',37000,5000,4500,2500,1);

  INSERT INTO poblacion
  VALUES ('555666777','Vicente','Marañón','Fernández','15/11/1978','Pz. América','10600','H',46000,8000,5000,4000,2);

INSERT INTO poblacion
  VALUES ('666777888','Beatriz','Losada','Gijón','12/04/1974','Av. Principal','06400','M',50000,15000,8000,5000,2);

INSERT INTO poblacion
  VALUES ('888999000','Fernando','Huertas','Martínez','30/05/1971','C. Mayor','06002','H',70000,20000,8000,4500,2);

INSERT INTO poblacion
  VALUES ('999000111','Francisco','Fernández','Merchán','12/03/1979','C. Poniente','10800','H',63000,12000,7500,4500,2);

INSERT INTO poblacion
  VALUES ('666999333','Paula','Ordóñez','Ruiz','01/02/1990','C. Atlántico','06800','M',25000,10000,3000,2000,2);

INSERT INTO poblacion
  VALUES ('987654321','Eva','Moreno','Pozo','10/05/1974','C. Justicia','10005','M',40000,9000,6000,3000,3);

INSERT INTO poblacion
  VALUES ('111000111','Antonio','Muñoz','Hernández','01/07/1989','C. Constitución','06800','H',25000,6500,3500,4000,3);

INSERT INTO poblacion
  VALUES ('111000222','Sara','Gálvez','Montes','07/04/1973','C. Cádiz','10300','M',40000,11000,9500,6500,3);

INSERT INTO poblacion
  VALUES ('111000333','Cristina','Corral','Palma','12/05/1976','C. Ermita','10600','M',48000,13000,7800,5200,3);

INSERT INTO poblacion
  VALUES ('111222333','Susana','Ruiz','Méndez','22/06/1999','Av. Libertad','10800','M',18000,5000,4500,2500,3);

INSERT INTO poblacion
  VALUES ('444555666','Ángel','Montero','Salas','07/04/2000','C. Tranquilidad','10300','H',14000,3000,3000,3000,4);

  INSERT INTO poblacion
  VALUES ('888777666','Manuel','Vega','Zarzal','23/11/1976','Pz. Azul','10005','H',36000,12000,6000,3000,4);

INSERT INTO poblacion
  VALUES ('333445555','Margarita','Guillén','Campos','19/03/1974','Av. Héroes','06800','M',50000,12000,7500,6500,4);

INSERT INTO poblacion
  VALUES ('222447777','Fermín','Hoz','Torres','08/08/1988','C. Curva','06002','H',25000,4000,3000,2500,4);