import mariadb

from error import (
    InvalidTableNameError,
    RequirementsNotMetError
)


def execute(connection, arguments):
    """This handles execution of all relevant arguments.

    :param connection: Database connection to run queries on
    :param arguments: Arguments passed to this program
    """
    cursor = connection.cursor()

    if arguments.show is not None:
        select_all(cursor, arguments.show)

    elif arguments.add is not None:
        # Dictionary of add functors and associated tables
        options = {
            'employee': add_employee
        }
        if arguments.add not in options.keys():
            msg = '{} is not a valid table'.format(arguments.add)
            raise InvalidTableNameError(msg)

        # Call appropriate functor
        options[arguments.add](cursor, arguments)

    connection.commit()  # This line saves the changes made to the database
    # Close connection once we're done with it
    cursor.close()
    connection.close()


def print_cursor(cursor):
    """Helper function to print results of a cursor

    :param cursor: Cursor iterator returned by calling cursor.execute()
    """
    for row in cursor:
        print(row)


def validate_command(arguments, required: list[str]):
    """Helper function to validate arguments passed to command line fit function being called.

    :param arguments: All arguments passed to the command line.
    :param required: List of required arguments.
    :return:
    """
    arg_dict = vars(arguments)
    print(arg_dict)

    not_met = list()
    for requirement in required:
        if arg_dict[requirement] is None:
            not_met.append(requirement)
    if len(not_met) != 0:
        msg = 'The following arguments are missing: {}'.format(not_met)
        raise RequirementsNotMetError(msg)


def select_all(cursor, table_name):
    """Show all tables or contents of a specific table

    Example:
        python main.py --show tables
        python main.py --show department

    :param cursor: cursor to mariadb
    :param table_name: Name of table to display
    """

    try:
        # Show tables
        if table_name == 'tables':
            cursor.execute('SHOW tables')
        # Show contents of specific tables
        else:
            cursor.execute(f'SELECT * from {table_name}')
        print_cursor(cursor)
    except mariadb.ProgrammingError:
        msg = '{} is not a valid table name'.format(table_name)
        print(msg)


def add_employee(cursor, arguments):
    required_args = ['first_name', 'last_name', 'number', 'job_id']
    validate_command(arguments, required_args)

    sql = 'INSERT INTO employee (first_name, last_name, phone, job_id) VALUES (?, ?, ?, ?)'
    values = (
        arguments.first_name,
        arguments.last_name,
        arguments.number,
        int(arguments.job_id)
    )
    print(values)
    cursor.execute(sql, values)


def remove_employee(cursor, arguments):
    pass

