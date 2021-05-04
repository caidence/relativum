#!/usr/bin/python

import mysql.connector, sys
from authenticator import Authenticator

def executeSQL(conn, first_name,last_name,pay_raise_percent):
    cursor = conn.cursor()
    query = "select * FROM employee where Last_Name = '" + last_name + "' AND First_Name = '" + first_name + "'"
    cursor.execute(query)
    result = cursor.fetchall()  
    employee_id = 0;  
    for row in result:
       employee_id = row[0]
    if (employee_id == 0):
       print('No records found')
       exit()
    pay = float(pay_raise_percent) + 1.00
    query = "update salary SET Gross_Salary = Gross_Salary * " + str(pay) +" WHERE Employee_ID = " + str(employee_id)
    cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    query = "select * FROM salary where Employee_ID = " + str(employee_id)
    cursor.execute(query)
    result = cursor.fetchall()  
    salary = 0
    for row in result:
       salary = row[3]
    print("Employee's New Salary: ",salary)

hostname = 'localhost'
username = 'root'
password = ''
database = 'payroll_management'

first_name = input('Enter employee first name: ')
last_name = input('Enter employee last name: ')
raise_percent = input('Enter the percent raise for employee: ')

pay_raise_percent = float(raise_percent)/100

connection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
executeSQL(connection, first_name, last_name, pay_raise_percent)
connection.close()