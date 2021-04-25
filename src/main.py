import argparse
import mariadb
import json
import os
from datetime import datetime
from getpass import getpass

from model import execute


class AuthenticationError(Exception):
    """Generic authentication error.
    """
    def __init__(self, message):
        super().__init__(message)


class GlobalArguments(object):
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
            '-c', action='store_true', dest='cache', help='Cache credentials', required=False, default=None)

    def __create_interaction_arguments(self):
        """Create arguments for interacting with the database.
        """
        self.parser.add_argument(
            '-s', '--show', action='store', dest='show', help='Show contents of a table', default=None)
        self.parser.add_argument(
            '-a', '--add', action='store', dest='add', help='Add a row to a table', default=None)

    def __create_general_arguments(self):
        self.parser.add_argument(
            '-f', '--firstname', action='store', dest='firstname', help='Employee first name', default=None)
        self.parser.add_argument(
            '-l', '--lastname', action='store', dest='lastname', help='Employee last name', default=None)
        self.parser.add_argument(
            '-N', '--number', action='store', dest='number', help='Phone number', default=None)
        self.parser.add_argument(
            '-j', '--job_id', action='store', dest='job_id', help='Employee job ID', default=None)
        self.parser.add_argument(
            '-H', '--hire_date', action='store', dest='hire_date', help='Employee hire date', default=datetime.now())
        self.parser.add_argument(
            '-L', '--leave_date', action='store', dest='leave_date', help='Employee leave date', default=datetime.now())


class Authenticator(object):
    def __init__(self, global_args):
        self._global_args = global_args
        self._args = self._global_args.args

    def __cache_credentials(self):
        """Cache credentials in cached.json
        """
        username = self._args.username if self._args.username is not None else input('Username: ')
        password = self._args.password if self._args.password is not None else getpass('Password: ')

        data = {
            'username': username,
            'password': password
        }
        with open('cached.json', 'w') as outfile:
            json.dump(data, outfile)

    @staticmethod
    def __load_cached_credentials(cred_dict) -> dict:
        """Load cached credentials from a file.

        :param cred_dict: Dictionary to upload credentials to.
        :return: Dictionary with updated credentials loaded from file.
        """
        with open('cached.json', 'r') as infile:
            credentials = json.load(infile)
        cred_dict.update({
            'user': credentials['username'],
            'password': credentials['password']
        })
        return cred_dict

    def authenticate(self):
        """Try to authenticate to the database with passed arguments.

        :return: mariadb.connection Connection to database if authentication succeeds
        """
        connection_kwargs = {
            'host': self._args.hostname,
            'database': self._args.database
        }

        if self._args.cache is not None:
            self.__cache_credentials()
            connection_kwargs = self.__load_cached_credentials(connection_kwargs)
        elif os.path.isfile('cached.json'):
            connection_kwargs = self.__load_cached_credentials(connection_kwargs)
        elif self._args.username is None or self._args.password is None:
            msg = 'No username, password, or cached credentials found'
            raise AuthenticationError(msg)
        else:
            connection_kwargs.update({
                'user': self._args.username,
                'password': self._args.password
            })

        try:
            db_connection = mariadb.connect(**connection_kwargs)
        except mariadb.OperationalError:
            message = 'Invalid username or password'
            raise AuthenticationError(message)
        except mariadb.ProgrammingError:
            message = 'Invalid database name "{}"'.format(connection_kwargs['database'])
            raise AuthenticationError(message)

        print('Successfully connected to {}.{}!'.format(connection_kwargs['host'], connection_kwargs['database']))
        return db_connection


if __name__ == '__main__':
    arguments = GlobalArguments()
    auth = Authenticator(arguments)
    connection = auth.authenticate()
    execute(connection, arguments.args)
