USE eftaz6n2sqv292f7;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE alumnos( 
    id_alumno integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_alumno varchar(80) NOT NULL,
    matricula varchar(20) NOT NULL,
    grupo varchar(20) NOT NULL,
    nombre_padre varchar(80) NOT NULL,
    direccion varchar(80) NOT NULL,
    telefono varchar(80) NOT NULL,
    id_telegram varchar(32) NOT NULL DEFAULT 'xxx'
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE asistencias( 
    id_asistencia integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_alumno integer NOT NULL,
    fecha timestamp,
    asistio varchar(2)NOT NULL,
    FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES 
('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('profesor',MD5(concat('profesor', 'kuorra_key')), 1, 1, 'Profesor', 'profesor@gmail.com','1A', MD5(concat('profesor', 'kuorra_key','2016/06/04')), 0);

INSERT INTO alumnos (nombre_alumno, matricula, grupo, nombre_padre, direccion, telefono, id_telegram)
VALUES
('Dejah Thoris','17161716','1A','Atg Thoris','Barsoon','7757512345','XXX'),
('Jhon Carter','17171717','1A','Jhon Thompson','Earth','7757512345','XXX'),
('Carthoris Carter','17181718','2A','Jhon Carter','Barsoon','7757512345','XXXX');

INSERT INTO asistencias (id_alumno, asistio)
VALUES
(1,'si'),
(2,'no'),
(3,'si');

SELECT * FROM users;
SELECT * FROM sessions;
SELECT * FROM alumnos;
SELECT * FROM asistencias;
