-- CREATE PAYROLL MANAGEMENT DATABASE

CREATE DATABASE payroll_management;

-- DROP EXISTING TABLE
DROP TABLE IF EXISTS salary;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS department;


-- CREATE EMPLOYEE TABLE
CREATE TABLE employee (
  Employee_ID INTEGER NOT NULL AUTO_INCREMENT,
  First_Name varchar(20) DEFAULT NULL,
  Last_Name varchar(20) DEFAULT NULL,
  Phone varchar(15) DEFAULT NULL,
  Department_ID INTEGER DEFAULT NULL,
  Joining_Date DATETIME NOT NULL,
  LeavingDate DATETIME NOT NULL,
  PRIMARY KEY (Employee_ID),
  FOREIGN KEY (Deparment_ID) REFERENCES Department(Deparmtnet_ID)
);

CREATE TABLE department (
	Department_ID INTEGER NOT NULL AUTO_INCREMENT,
    Department_Name VARCHAR(50),
    PRIMARY KEY (Department_ID)
);

CREATE TABLE salary (
	ID INTEGER NOT NULL AUTO_INCREMENT,
    Employee_ID INTEGER,
    Department_ID INTEGER,
    Job_ID INTEGER,
    Salary NUMERIC(12,2),
    PRIMARY KEY (ID),
    FOREIGN KEY (Employee_ID) REFERENCES employee(Employee_ID),
    FOREIGN KEY (Department_ID) REFERENCES department(Department_ID),
    FOREIGN KEY (Job_ID) REFERENCES job(Job_ID)
);
