USE RbChrono;

DROP TABLE IF EXISTS Competitors;

CREATE TABLE Competitors(
 Id int PRIMARY KEY,
 Name nvarchar(256) NOT NULL,
 CarModel nvarchar(256),
 StartNumber int,
 Class int,
 ClassText nvarchar (50)
);

