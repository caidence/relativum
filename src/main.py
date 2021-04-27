# Python imports
import argparse

# Local imports
from authenticator import Authenticator
from model import execute


class GlobalArguments(object):
    """Separate argument definitions from argument sterilization. Simplifies writing tests.
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.__create_authentication_args()
        self.__create_interaction_arguments()
        self.__create_general_arguments()

        self.args = self.parser.parse_args()

    def __create_authentication_args(self):
        """Create basic arguments for authenticating to database.
        """
        self.parser.add_argument(
            '-u', '--username', action='store', dest='username', help='Database username', default=None)
        self.parser.add_argument(
            '-p', '--password', action='store', dest='password', help='Database password', default=None)
        self.parser.add_argument(
            '-n', '--hostname', action='store', dest='hostname', help='Database hostname', default='localhost')
        self.parser.add_argument(
            '-d', '--database', action='store', dest='database', help='Database name', default='payroll_management')
        self.parser.add_argument(
            '-c', '--cache', action='store_true', dest='cache', help='Cache credentials', required=False, default=None)

    def __create_interaction_arguments(self):
        """Create arguments for interacting with the database.
        """
        self.parser.add_argument(
            '-s', '--show', action='store', dest='show', help='Show contents of a table', default=None,
            choices=['job', 'department', 'employee', 'tables', 'salary'])
        self.parser.add_argument(
            '-a', '--add', action='store', dest='add', help='Add a row to a table', default=None,
            choices=['job', 'department', 'employee', 'salary'])
        self.parser.add_argument(
            '-r', '--remove', action='store', dest='remove', help='Remove a row from a table', default=None,
            choices=['job', 'department', 'employee', 'salary'])
        self.parser.add_argument(
            '-U', '--update', action='store', dest='update', help='Update a row in a table', default=None,
            choices=['job', 'department', 'employee', 'salary'])
        self.parser.add_argument(
            '--set_fn', action='store', dest='set_first_name', help='Set first name', default=None)
        self.parser.add_argument(
            '--set_ln', action='store', dest='set_last_name', help='Set last name', default=None)
        self.parser.add_argument(
            '--set_phone', action='store', dest='set_phone', help='Set employee phone number', default=None)
        self.parser.add_argument(
            '--set_job_id', action='store', dest='set_job_id', help='Set employee job ID', default=None)
        self.parser.add_argument(
            '--set_name', action='store', dest='set_department_name', help='Set department name', default=None)
        self.parser.add_argument(
            '--set_title', action='store', dest='set_job_title', help='Set job title', default=None)
        self.parser.add_argument(
            '--set_department_id', action='store', dest='set_department_id', help='Set department ID', default=None)

    def __create_general_arguments(self):
        """Create general arguments for interacting with the database.
        """
        self.parser.add_argument(
            '-f', '--first_name', action='store', dest='first_name', help='Employee first name', default=None)
        self.parser.add_argument(
            '-l', '--last_name', action='store', dest='last_name', help='Employee last name', default=None)
        self.parser.add_argument(
            '-N', '--phone', action='store', dest='phone', help='Phone number', default=None)
        self.parser.add_argument(
            '-j', '--job_id', action='store', dest='job_id', help='Employee job ID', default=None)
        self.parser.add_argument(
            '-e', '--employee_id', action='store', dest='employee_id', help='Employee ID', default=None)
        self.parser.add_argument(
            '-D', '--department_name', action='store', dest='department_name', help='Department name', default=None)
        self.parser.add_argument(
            '-i', '--department_id', action='store', dest='department_id', help='Department ID', default=None)
        self.parser.add_argument(
            '-t', '--job_title', action='store', dest='job_title', help='Job title', default=None)


if __name__ == '__main__':
    arguments = GlobalArguments()  # We need to pass these to execution
    auth = Authenticator(arguments)  # Authenticate to the database
    connection = auth.authenticate()  # Open a connection to the database
    execute(connection, arguments.args)  # Sterilize and process the user arguments
