import mariadb
import enum


class TablesName(enum.Enum):
    """Payroll management table names
    """
    employee = 'employee'


class InvalidTableNameError(Exception):
    def __init__(self, message):
        super().__init__(message)


class RequirementsNotMetError(Exception):
    def __init__(self, message):
        super().__init__(message)


def execute(connection, arguments):
    """This handles execution of all relevant arguments.

    :param connection: Database connection to run queries on
    :param arguments: Arguments passed to this program
    """

    if arguments.show is not None:
        select_all(connection, arguments.show)

    elif arguments.add is not None:
        # Dictionary of add functors and associated tables
        options = {
            'employee': add_employee
        }
        if arguments.add not in options.keys():
            msg = '{} is not a valid table'.format(arguments.add)
            raise InvalidTableNameError(msg)

        # Call appropriate functor
        options[arguments.add](connection, arguments)

    # Close connection once we're done with it
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


def select_all(connection, table_name):
    """Show all tables or contents of a specific table

    Example:
        python main.py --show tables
        python main.py --show department

    :param connection: Connection to mariadb
    :param table_name: Name of table to display
    """
    cursor = connection.cursor()

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
    finally:
        cursor.close()


def add_employee(connection, arguments):
    required_args = ['firstname', 'lastname', 'number', 'job_id', 'hire_date']
    validate_command(arguments, required_args)

    cursor = connection.cursor()
    table_name = TablesName.employee.value

    try:
        sql = f'INSERT INTO {table_name} ' \
              f'(First_Name, Last_Name, Phone, Job_ID, Joining_Date, LeavingDate) ' \
              f'VALUES (?, ?, ?, ?, ?, ?)'
        values = (
            arguments.firstname,
            arguments.lastname,
            arguments.number,
            arguments.job_id,
            arguments.hire_date,
            None  # Leave date will be NULL since we're adding an employee
        )
        cursor.execute(sql, values)
        for x in cursor:
            print(x)
    finally:
        cursor.close()


def remove_employee(connection, arguments):
    pass

