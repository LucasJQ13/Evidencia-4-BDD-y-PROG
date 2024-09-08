
CREATE DATABASE Evidencia_4;
USE Evidencia_4;
-- Proyector atributos
CREATE TABLE Proyector (
proyector_id int(100) primary key AUTO_INCREMENT,
modelo VARCHAR(100),
resolucion_actual VARCHAR(10),
conexion_inalambrica BOOLEAN
);


-- Dispositivos conectados
CREATE TABLE Dispositivos (
dispositivo_id int primary key AUTO_INCREMENT,
nombre_dispositivo VARCHAR(100),
proyector_id INTEGER,
foreign key (proyector_id) references Proyector(proyector_id)
);

-- Resoluciones disponibles
CREATE TABLE Resoluciones(
resolucion_id INT primary key AUTO_INCREMENT,
resolucion VARCHAR(50),
proyector_id INTEGER,
foreign key (proyector_id) references Proyector(proyector_id)
);

-- Conexion Inalambrica
CREATE TABLE ConexionesInalambricas (
conexion_id INT primary key AUTO_INCREMENT,
proyector_id INT,
estado BOOLEAN,
fecha_conexion timestamp,
foreign key (proyector_id) references Proyector(proyector_id)
);

-- Sentencias INSERT
INSERT INTO Proyector (modelo, resolucion_actual, conexion_inalambrica)
VALUES ('VR-ISPC-24', '720p', TRUE);

INSERT INTO Proyector (modelo, resolucion_actual, conexion_inalambrica)
VALUES ('VR-ISPC-24', '1080p', FALSE);

INSERT INTO Proyector (modelo, resolucion_actual, conexion_inalambrica)
VALUES ('VR-ISPC-24', '1440p', TRUE);


INSERT INTO Dispositivos (nombre_dispositivo, proyector_id)
VALUES ('Celular', 1);

INSERT INTO Dispositivos (nombre_dispositivo, proyector_id)
VALUES ('PC', 1);

INSERT INTO Dispositivos (nombre_dispositivo, proyector_id)
VALUES ('Notebook', 1);


INSERT INTO Resoluciones (resolucion, proyector_id)
VALUES ('720P', 1);

INSERT INTO Resoluciones (resolucion, proyector_id)
VALUES ('1080P', 1);

INSERT INTO Resoluciones (resolucion, proyector_id)
VALUES ('1440P', 1);


INSERT INTO ConexionesInalambricas (proyector_id, estado, fecha_conexion)
VALUES (1, TRUE, '2024-09-05 19:00:00');

INSERT INTO ConexionesInalambricas (proyector_id, estado, fecha_conexion)
VALUES (1, FALSE, '2024-09-06 23:30:00');

INSERT INTO ConexionesInalambricas (proyector_id, estado, fecha_conexion)
VALUES (1, TRUE, '2024-09-07 18:00:00');

-- Consultas SELECT
SELECT * FROM Proyector WHERE conexion_inalambrica = TRUE;
SELECT * FROM Dispositivos WHERE proyector_id = 1;
SELECT proyector_id, COUNT(*) AS cantidad_dispositivos FROM Dispositivos GROUP BY proyector_id;
SELECT * FROM ConexionesInalambricas WHERE proyector_id = 1 ORDER BY fecha_conexion;
SELECT proyector_id, COUNT(*) AS veces_activa FROM ConexionesInalambricas WHERE proyector_id = 1 AND estado = TRUE;

