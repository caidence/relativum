# reletivum
Payroll Management CS-665
=========================

## Getting started
-------------------

First, let's cache your database credentials. There are two ways:

1. Passing your database username and password to the program
```bash
python main.py --username <your_username> --password <your_password> --cache
```

2. If you don't want your password showing up in the command history, you can cache your credentials interactivly by typing
```bash
python main.py -c
```

## Showing contnets of a table

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

## Adding an employee

There are several ways to add an employee, hopefully the examples make these ways clear. Be sure to pass all
**Required arguments** for --add employee. They are: --first_name (or -f), --last_name (or -l), --number (or -N), --job_id (or -j)

```bash
# The following two commands do the same thing
python main.py --add employee --first_name Joe --last_name Smith --number 555-555-5555 --job_id 3
python main.py -a employee -f Joe -l Smith -N 555-555-5555 -j 3
```

## Removing an employee

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
