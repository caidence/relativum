-- CREATE PAYROLL MANAGEMENT DATABASE
DROP DATABASE IF EXISTS `payroll_management`;
CREATE DATABASE payroll_management;
USE payroll_management;

-- DROP EXISTING TABLE
DROP TABLE IF EXISTS salary;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS job;
DROP TABLE IF EXISTS department;

-- CREATE DEPARTMENT TABLE
CREATE TABLE department (
	Department_ID INTEGER NOT NULL AUTO_INCREMENT,
    Department_Name VARCHAR(50),
    PRIMARY KEY (Department_ID)
);
INSERT INTO department VALUES
(1, 'Administration'),
(2, 'Sales'),
(3, 'Accounting'),
(4, 'Human Resource'),
(5, 'Customer Service');

-- CREATE JOB TABLE
CREATE TABLE job (
	Job_ID INTEGER NOT NULL AUTO_INCREMENT,
    Department_ID INTEGER NOT NULL,
	Job_Title VARCHAR(50),
    PRIMARY KEY (Job_ID),
    FOREIGN KEY (Department_ID) References department(Department_ID)
);
INSERT INTO job VALUES
(1,1,'Regional Manager'),
(2,2,'Salesman'),
(3,1,'Receptionist'),
(4,3,'Senior Accountant'),
(5,3,'Accountant'),
(6,5,'Customer Service Representative'),
(7,4,'Human Resources Representative');

-- CREATE EMPLOYEE TABLE
CREATE TABLE employee (
  Employee_ID INTEGER NOT NULL AUTO_INCREMENT,
  First_Name varchar(20) NOT NULL,
  Last_Name varchar(20) NOT NULL,
  Phone varchar(15) NOT NULL,
  Job_ID INTEGER DEFAULT NULL,
  Joining_Date DATE NOT NULL,
  LeavingDate DATE NULL,
  PRIMARY KEY (Employee_ID),
  FOREIGN KEY (Job_ID) REFERENCES job(Job_ID)
);
INSERT INTO employee VALUES
(1, 'Michael', 'Scott', '123-123-1234',1, '2021-04-19', NULL),
(2, 'Jim', 'Halpert', '456-456-4567',2,'2021-04-19', NULL),
(3, 'Dwight', 'Schrute', '717-555-0177',2,'2021-04-19', NULL),
(4, 'Pam', 'Beesley', '717-333-0177',3,'2021-04-19', NULL),
(5, 'Angela', 'Martin', '717-333-0177',3,'2021-04-19', NULL),
(6, 'Stanley', 'Hudson', '717-333-0177',2,'2021-04-19', NULL),
(7, 'Phyllis', 'Vance', '717-333-0177',2,'2021-04-19', NULL),
(8, 'Andrew', 'Bernard', '717-333-0177',2,'2021-04-19', NULL),
(9, 'Kevin', 'Malone', '717-333-0177',5,'2021-04-19', NULL),
(10, 'Oscar', 'Martinez', '717-333-0177',5,'2021-04-19', NULL),
(11, 'Kelly', 'Kapoor', '717-333-0177',6,'2021-04-19', NULL),
(12, 'Toby', 'Flenderson', '717-333-0177',7,'2021-04-19', NULL);

-- CREATE SALARY TABLE
CREATE TABLE salary (
	Salary_ID INTEGER NOT NULL AUTO_INCREMENT,
    Employee_ID INTEGER NOT NULL,
    State_Tax DECIMAL (4,4) NOT NULL,
    Gross_Salary NUMERIC(12,2) NOT NULL,
    Net_Salary NUMERIC(12,2) NOT NULL,
    PRIMARY KEY (Salary_ID),
    FOREIGN KEY (Employee_ID) REFERENCES employee(Employee_ID)
);
INSERT INTO salary VALUES
(1,1,0.0307,60000.00,58158.00),
(2,2,0.0307,48000.00,46526.40),
(3,3,0.0307,48000.00,46526.40),
(4,4,0.0307,35000.00,33925.50),
(5,5,0.0307,57000.00,55250.10),
(6,6,0.0307,48000.00,46526.40),
(7,7,0.0307,48000.00,46526.40),
(8,8,0.0307,48000.00,46526.40),
(9,9,0.0307,50000.00,48465.00),
(10,10,0.0307,50000.00,48465.00),
(12,12,0.0307,58800.00,56994.84);
