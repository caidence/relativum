# Local imports
from helper import (
    add_helper,
    update_helper,
    remove_helper
)


def execute(connection, arguments):
    """This handles execution of all relevant arguments.

    :param connection: Database connection to run queries on
    :param arguments: Arguments passed to this program
    """
    cursor = connection.cursor()

    # Simulates vector of unordered maps of function pointers
    functors = {
        'employee': {
            'add': add_employee,
            'remove': remove_employee,
            'update': update_employee},
        'department': {
            'add': add_department,
            'remove': remove_department,
            'update': update_department},
        'job': {
            'add': add_job,
            'remove': remove_job,
            'update': update_job}
    }

    # Call the appropriate functor object
    if arguments.show is not None:
        select_all(cursor, arguments.show)
    elif arguments.add is not None:
        functors[arguments.add]['add'](cursor, arguments)
    elif arguments.remove is not None:
        functors[arguments.remove]['remove'](cursor, arguments)
    elif arguments.update is not None:
        functors[arguments.update]['update'](cursor, arguments)

    connection.commit()  # This line saves the changes made to the database
    # Close connection once we're done with it
    cursor.close()
    connection.close()


def add_employee(cursor, arguments):
    """Add an employee to the employee table.

    Examples:
        python main.py --add employee -f Joe -l Smith -N 555-555-5555 -j 3
        python main.py --add employee --first_name Joe --last_name Smith --number 555-555-5555 --job_id 3

    :param cursor: Cursor for SQL command execution.
    :param arguments: All arguments passed to program.
    """
    required_args = ('first_name', 'last_name', 'phone', 'job_id')
    add_helper(cursor, arguments, required_args, 'employee')


def update_employee(cursor, arguments):
    """Update an employee.

    Examples:
        python main.py --update employee --employee_id 14 --set_fn Joe
        python main.py --update employee --first_name Bob --set_ln George

    :param cursor: Cursor for SQL command execution.
    :param arguments: All arguments passed to program.
    """
    valid_arguments = ('first_name', 'last_name', 'phone', 'job_id', 'employee_id')
    update_arguments = ('set_first_name', 'set_last_name', 'set_phone', 'set_job_id')
    update_helper(cursor, arguments, valid_arguments, update_arguments, 'employee')


def remove_employee(cursor, arguments):
    """Remove an employee from the employee table.

    Examples:
        python main.py --remove employee --first_name Joe
        python main.py -r employee --last_name smith
        python main.py -r employee --employee_id 7
        python main.py -r employee -e 7

    :param cursor: Cursor for SQL command execution.
    :param arguments: All arguments passed to program.
    """
    valid_args = ('first_name', 'last_name', 'employee_id')
    remove_helper(cursor, arguments, valid_args, 'employee')


def add_department(cursor, arguments):
    """Add a department to the department table.

    Examples:
        python main.py --add department --department_name NewDepartment
        python main.py -a department -D NewDepartment

    :param cursor: Cursor for SQL command execution.
    :param arguments: All arguments passed to program.
    """
    required_args = ('department_name',)
    add_helper(cursor, arguments, required_args, 'department')


def update_department(cursor, arguments):
    """Update a department.

        Examples:
            python main.py --update department --department_id 3 --set_name NewName
            python main.py -u department -i 3 --set_name NewName

        :param cursor: Cursor for SQL command execution.
        :param arguments: All arguments passed to program.
        """
    valid_arguments = ('department_name', 'department_id')
    update_arguments = ('set_department_name',)
    update_helper(cursor, arguments, valid_arguments, update_arguments, 'department')


def remove_department(cursor, arguments):
    """Remove a department from department table.

    Exampes:
        python main.py --remove department --department_name NewDepartment
        python main.py -r department -D NewDepartment

        python main.py --remove department --department_id 7
        python main.py -r department -i 7

    :param cursor: Cursor for SQL command execution.
    :param arguments: All arguments passed to program.
    """
    valid_args = ('department_id', 'department_name')
    remove_helper(cursor, arguments, valid_args, 'department')


def add_job(cursor, arguments):
    """Add a job to the job table.

    Examples:
        python main.py --add job --job_title NewJob --department_id 5
        python main.py -a job -t NewJob -i 5

    :param cursor: Cursor for SQL command execution.
    :param arguments: All arguments passed to program.
    """
    required_args = ('department_id', 'job_title')
    add_helper(cursor, arguments, required_args, 'job')


def update_job(cursor, arguments):
    """Update a job.

        Examples:
            python main.py --update job --job_title sales --set_department_id 5
            python main.py -u job -t sales --set_department_id 5

        :param cursor: Cursor for SQL command execution.
        :param arguments: All arguments passed to program.
        """
    valid_arguments = ('job_title', 'job_id')
    update_arguments = ('set_job_title', 'set_department_id')
    update_helper(cursor, arguments, valid_arguments, update_arguments, 'job')


def remove_job(cursor, arguments):
    """Remove a job from job table.

    Examples:
        python main.py --remove job --job_id 7
        python main.py -r job -j 7

        python main.py --remove job --job_title sales
        python main.py -r job -t sales

    :param cursor: Cursor for SQL command execution.
    :param arguments: All arguments passed to program.
    """
    valid_args = ('job_title', 'job_id')
    remove_helper(cursor, arguments, valid_args, 'job')


def select_all(cursor, table_name):
    """Show all tables or contents of a specific table

    Examples:
        python main.py --show tables
        python main.py -s department

    :param cursor: cursor to mariadb
    :param table_name: Name of table to display
    """
    if table_name == 'tables':
        cursor.execute('SHOW tables')
    else:
        cursor.execute(f'SELECT * from {table_name}')
    for row in cursor:
        print(row)
