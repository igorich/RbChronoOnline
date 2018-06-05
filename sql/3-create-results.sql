USE RbChrono;

DROP TABLE IF EXISTS Results;

create table Results (
 Id int PRIMARY KEY,
 CompetitorId int NOT NULL,
 RaceId int NOT NULL,
 ResultText varchar (256),
 ResultTime datetime,
 FOREIGN KEY (RaceId) REFERENCES Races(Id),
 FOREIGN KEY (CompetitorId) REFERENCES Competitors(Id)
);

