-- CREATE PAYROLL MANAGEMENT DATABASE
DROP DATABASE IF EXISTS `payroll_management`;
CREATE DATABASE payroll_management;
USE payroll_management;

-- DROP EXISTING TABLE
DROP TABLE IF EXISTS salary;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS job;
DROP TABLE IF EXISTS department;


/*
    @brief  This table contains department information
    @param  department_id (primary key) Id of department
    @param  department_name name of department
*/
CREATE TABLE department (
    department_id INTEGER NOT NULL AUTO_INCREMENT,
    department_name VARCHAR(50),
    PRIMARY KEY (department_id)
);
INSERT INTO department (department_name) VALUES
('Administration'),
('Sales'),
('Accounting'),
('Human Resource'),
('Customer Service');


/*
    @brief  This table contains information about different jobs
    @param  job_id (primary key) Holds the ID of associated job
    @param  department_id ID of department, must be in department.department_id
    @param  job_title Friendly name of job
*/
CREATE TABLE job (
    job_id INTEGER NOT NULL AUTO_INCREMENT,
    department_id INTEGER NOT NULL,
    job_title VARCHAR(50) NOT NULL,
    PRIMARY KEY (job_id),
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);
INSERT INTO job (department_id, job_title) VALUES
(1, 'Regional Manager'),
(2, 'Salesman'),
(1, 'Reception'),
(3, 'Accountant'),
(5, 'Customer Service Representative'),
(4, 'Human Resources Representative');



/*
    @brief  This table keeps track of current employees
    @param  employee_id (primary key) Unique employee identifier
    @param  first_name First name of employee
    @param  last_name Last name of employee
    @param  phone Employee's company phone number
    @param  job_id Employee's job id, must be in job.job_id
*/
CREATE TABLE employee (
    employee_id INTEGER NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    job_id INTEGER NOT NULL,
    PRIMARY KEY (employee_id),
    FOREIGN KEY (job_id) REFERENCES job(job_id)
);
INSERT INTO employee (first_name, last_name, phone, job_id) VALUES
('Michael', 'Scott', '123-123-1234', 1),
('Jim', 'Halpert', '456-456-4567', 2),
('Dwight', 'Schrute', '717-555-0177', 2),
('Pam', 'Beesley', '717-333-0177', 3),
('Angela', 'Martin', '717-333-0177', 4),
('Stanley', 'Hudson', '717-333-0177', 2),
('Phyllis', 'Vance', '717-333-0177', 2),
('Andrew', 'Bernard', '717-333-0177', 2),
('Kevin', 'Malone', '717-333-0177', 4),
('Oscar', 'Martinez', '717-333-0177', 4),
('Kelly', 'Kapoor', '717-333-0177', 5),
('Toby', 'Flenderson', '717-333-0177', 6);



/*
    @brief  This table holds salary information for employees
    @param  payroll_id (primary key) Employee's payroll id
    @param  employee_id Employee's id, must be in employee.employee_id
    @param  gross_salary Employee salary before tax
*/
CREATE TABLE salary (
    payroll_id INTEGER NOT NULL AUTO_INCREMENT,
    employee_id INTEGER NOT NULL,
    gross_salary NUMERIC(12, 2) NOT NULL,
    PRIMARY KEY (payroll_id),
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);
INSERT INTO salary (employee_id, gross_salary) VALUES
(1, 60000.00),
(2, 48000.00),
(3, 48000.00),
(4, 35000.00),
(5, 57000.00),
(6, 48000.00),
(7, 48000.00),
(8, 48000.00),
(9, 50000.00),
(10, 50000.00),
(11, 51000.00),
(12, 58800.00);
