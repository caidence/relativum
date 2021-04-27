# Python imports
import json
import os
from getpass import getpass

# Third-party imports
import mariadb

# Local imports
from error import AuthenticationError


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
