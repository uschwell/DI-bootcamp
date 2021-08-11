CREATE TABLE Person
(
Personal_Id INT PRIMARY KEY,
Person_Name VARCHAR(255),
EmailId VARCHAR(255)
);

CREATE TABLE Person_Taxes
(
Passport_Id INT PRIMARY KEY,
Total_Income VARCHAR(255),
Personal_Id INT,
FOREIGN KEY REFERENCES Person(Personal_Id)
);


SELECT Person.Personal_Id, Person.Person_Name,Person.EmailId, Person_Taxes.Passport_Id, Person_Taxes.Total_Income
FROM Person
LEFT JOIN Person_Taxes
ON Person.Personal_Id=Person_Taxes.Personal_id;


SELECT Person.Personal_Id, Person.Person_Name,Person.EmailId, Person_Taxes.Passport_Id, Person_Taxes.Total_Income
FROM Person
Right JOIN Person_Taxes
ON Person.Personal_Id=Person_Taxes.Personal_id;


SELECT Person.Personal_Id, Person.Person_Name,Person.EmailId, Person_Taxes.Passport_Id, Person_Taxes.Total_Income
FROM Person
INNER JOIN Person_Taxes
ON Person.Personal_Id=Person_Taxes.Personal_id;


SELECT Person.Personal_Id, Person.Person_Name,Person.EmailId, Person_Taxes.Passport_Id, Person_Taxes.Total_Income
FROM Person
FULL OUTER JOIN Person_Taxes
ON Person.Personal_Id=Person_Taxes.Personal_id;