USE RbChrono;

DROP TABLE IF EXISTS Competitors;

create table Competitors (
 Id int PRIMARY KEY,
 UniqKey int,
 Name varchar (256) NOT NULL,
 Car varchar (256),
 Team varchar (256),
 Points int,
 StartNumber int,
);

