import argparse
import mariadb


class AuthenticationError(Exception):
    """Generic authentication error.
    """
    def __init__(self, message):
        super().__init__(message)


class Database(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self.__create_authentication_args()
        self._args = self._parser.parse_args()

        self.authenticate()

    def __create_authentication_args(self):
        """Create basic arguments for authenticating to database.
        """
        self._parser.add_argument(
            '-u', action='store', dest='username', help='Database username', required=True)
        self._parser.add_argument(
            '-p', action='store', dest='password', help='Database password', required=True)
        self._parser.add_argument(
            '-d', action='store', dest='database', help='Database name', default='payroll_management')
        self._parser.add_argument(
            '-n', action='store', dest='hostname', help='Hostname or IP address', default='localhost')

    # TODO: create credential cache
    def authenticate(self):
        """Try to authenticate to the database with passed arguments.

        :return: mariadb.connection Connection to database if authentication succeeds
        """
        connection_kwargs = {
            'host': self._args.hostname,
            'user': self._args.username,
            'password': self._args.password,
            'database': self._args.database
        }
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
    database = Database()
    connection = database.authenticate()

