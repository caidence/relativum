-- CREATE PAYROLL MANAGEMENT DATABASE

CREATE DATABASE payroll_management;

-- DROP EXISTING TABLE
DROP TABLE IF EXISTS salary;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS job;
DROP TABLE IF EXISTS department;


-- CREATE EMPLOYEE TABLE
CREATE TABLE employee (
  Employee_ID INTEGER NOT NULL AUTO_INCREMENT,
  First_Name varchar(20) NOT NULL,
  Last_Name varchar(20) NOT NULL,
  Address varchar(50) NOT NULL,
  Phone varchar(15) NOT NULL,
  Department_ID INTEGER DEFAULT NULL,
  Joining_Date DATETIME NOT NULL,
  LeavingDate DATETIME NOT NULL,
  PRIMARY KEY (Employee_ID),
  FOREIGN KEY (Deparment_ID) REFERENCES department(Deparmtnet_ID)
);

CREATE TABLE department (
	Department_ID INTEGER NOT NULL AUTO_INCREMENT,
    Department_Name VARCHAR(50),
    PRIMARY KEY (Department_ID)
);

CREATE TABLE job (
	Job_ID INTEGER NOT NULL AUTO_INCREMENT,
    Department_ID VARCHAR(50),
	Job_Title VARCHAR(50),
    PRIMARY KEY (Job_ID),
    FOREIGN KEY (Department_ID) References department(Department)
);

CREATE TABLE salary (
	Salary_ID INTEGER NOT NULL AUTO_INCREMENT,
    Employee_ID INTEGER NOT NULL,
    Department_ID INTEGER NOT NULL,
    Job_ID INTEGER NOT NULL,
    Tax NUMERIC (0,4) NOT NULL,
    Gross_Salary NUMERIC(12,2) NOT NULL,
    Net_Salary NUMERIC(12,2) NOT NULL,
    PRIMARY KEY (Salary_ID),
    FOREIGN KEY (Employee_ID) REFERENCES employee(Employee_ID),
    FOREIGN KEY (Department_ID) REFERENCES department(Department_ID),
    FOREIGN KEY (Job_ID) REFERENCES job(Job_ID)
);