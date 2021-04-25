import argparse
import mariadb
import json
import os
from getpass import getpass


class AuthenticationError(Exception):
    """Generic authentication error.
    """
    def __init__(self, message):
        super().__init__(message)


class GlobalArguments(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.__create_authentication_args()

        self.args = self.parser.parse_args()

    def __create_authentication_args(self):
        """Create basic arguments for authenticating to database.
        """
        self.parser.add_argument(
            '-u', action='store', dest='username', help='Database username', required=False, default=None)
        self.parser.add_argument(
            '-p', action='store', dest='password', help='Database password', required=False, default=None)
        self.parser.add_argument(
            '-d', action='store', dest='database', help='Database name', default='payroll_management')
        self.parser.add_argument(
            '-n', action='store', dest='hostname', help='Hostname or IP address', default='localhost')
        self.parser.add_argument(
            '-c', action='store_true', dest='cache', help='Cache credentials', required=False, default=None)


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

        return db_connection


if __name__ == '__main__':
    arguments = GlobalArguments()
    auth = Authenticator(arguments)
    session = auth.authenticate()
