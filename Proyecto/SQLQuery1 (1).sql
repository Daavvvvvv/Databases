CREATE TABLE Libro (
id_Libro    int Not Null Primary Key ,
Titulo		varchar (999),
Editorial	varchar (999),
Area		varchar (999),
diasPrest int 
);

CREATE TABLE Autor (
id_Autor        int not null Primary Key,
Nombre          varchar (999),
);

CREATE TABLE LibAut (
id_Autor    int not null references Autor,
id_Libro	int not null references Libro
primary key (id_Autor, id_Libro)
);

CREATE TABLE Estudiante (
id_Lector    int not null Primary Key,
CI            varchar (999),
Nombre        varchar (999),
Direccion    varchar (999),
Carrera        varchar (999),
Edad        smallint,
Lib_Prestados int
);

create table Prestamo(
id_Lector int NOT NULL references Estudiante,
id_Libro  int NOT NULL references Libro,
FechaDevolucion date,
FechaPrestamo date NOT NULL, 
primary key(id_Lector),
FOREIGN KEY(id_Libro) REFERENCES Libro (id_Libro)
)


CREATE TABLE MultEst(
id_Lector int primary key not null references Estudiante,
Devolucion bit not null,
valorMulta int 
);

CREATE TABLE Editorial(
id_Libro int not null references Libro,
Editorial varchar (10),
Nombre_Editorial varchar (999)
primary key(id_Libro,Editorial)
)