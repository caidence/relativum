# relativum -- Latin (adjective) In relation to
------------------------------------------------
# Table of Contents
- [General](#general)
  * [Setup](#setup)
  * [Getting started](#getting-started)
  * [Help](#help)
  * [Showing tables](#showing-tables)
- [Employee table](#employee)
  * [Adding an employee](#adding-an-employee)
  * [Update an employee](#update-an-employee)
  * [Removing an employee](#removing-an-employee)
- [Department table](#department)
  * [Adding a department](#adding-a-department)
  * [Removing a department](#removing-a-department)

## General
----------------------------------

### Setup
Setup is simple: clone the repository then run the setup script :smile: that's it!
```bash
git clone https://github.com/caidence/relativum.git
python relativum/setup/setup.py
```

setup.py detects your opperating system and will setup your env accoiringly.

### Getting started

First, let's cache your database credentials. There are two ways:

1. Passing your database username and password to the program
```bash
python main.py --username <your_username> --password <your_password> --cache
```

2. If you don't want your password showing up in the command history, you can cache your credentials interactivly by typing
```bash
python main.py -c
```

### Help
Get help by typing
```bash
# The following commands are equal
python main.py -h
python main.py --help
```

### Showing tables

There are two functions of the --show argument: to show all tables, to show the contents of a specific table.

Show *all tables* by executing one of the following
```bash
python main.py --show tables
python main.py -s tables
```

Show the contents of a *specific table* by executing one of the fillowing
```bash
# Shows contents of employee table
python main.py --show employee

# Shows contents of department table
python main.py -s department
```

## Employee
------------------------------------

### Adding an employee

There are several ways to add an employee, hopefully the examples make these ways clear. Be sure to pass all
**Required arguments** for --add employee. They are: --first_name (or -f), --last_name (or -l), --number (or -N), --job_id (or -j)

```bash
# The following two commands do the same thing
python main.py --add employee --first_name Joe --last_name Smith --number 555-555-5555 --job_id 3
python main.py -a employee -f Joe -l Smith -N 555-555-5555 -j 3
```

### Update an employee

You can update an existing employee's attributes using the --update command.
```bash
# Change employee with ID 14 to have first name "Joe"
python main.py --update employee --employee_id 14 --set_fn Joe
```

You don't have to update by employee ID, you can update by names, too.
```bash
# Update users with first name "Bob" to have last name "George"
python main.py --update employee --first_name Bob --set_ln George
# Same as previous command
python main.py -u employee -f Bob --set_ln George
```

Another feature is that you can update as many attributes at a time as you want!
```bash
# The following are equal
python main.py --update employee --employee_id 14 --set_fn Joe --set_ln Smith --set_salary 50000.00
python main.py -u employee -e 14 --set_fn Joe --set_ln Smith --set_salary 50000.00
```

### Removing an employee

You can remove an employee using their first name, last name, or employee ID. When removing an employee, make sure you only specify **one** attribute (first name, lastname, or enployee ID). If removing by first name or last name, case does not matter (i.e. Joe is treated the same as jOE)
```bash
# Remove employee by first name (both do the same thing)
python main.py --remove employee --first_name Joe
python main.py -r -f Joe

# Remove employee by last name (both do the same thing)
python main.py --remove employee --last_name Smith
python main.py -r -l Smith

# Remove employee by ID
python main.py --remove employee --employee_id 12
python main.py -r employee -e 12
```
**Note:** It is recommended to remove employees by their employee ID since removing by first name or last name will remove **ALL** employees with that name.

## Department
----------------------------------------

### Adding a department

Adding departments is similar to adding an employee. However, the only **required argument** is --department_name (or -D). Here are some exampes:
```bash
# Add department using long and short arguments
python main.py --add department --department_name NewDepartment
python main.py -a department -D NewDepartment
```

### Removing a department

Similarly, you can remove a department by name or ID with the following commands.
```bash
# Remove department by name
python main.py --remove department --department_name NewDepartment
python main.py -r department -D NewDepartment

# Remove department by ID
python main.py --remove department --department_id 7
python main.py -r department -i 7
```
