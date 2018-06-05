USE RbChrono;

DROP TABLE IF EXISTS Races;

CREATE TABLE Races ( 
    Id int NOT NULL AUTO_INCREMENT ,
    Name varchar(256) NOT NULL, 
    Description text, 
    RaceStartTime datetime NOT NULL,
    PRIMARY KEY (Id)
);
