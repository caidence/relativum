import subprocess
import os
from getpass import getpass


if __name__ == '__main__':
    print('Setting up your environment, this may take some time...')

    # Windows
    if os.name == 'nt':
        commands = (
            ['python', '-m', 'pip', 'install', '-r', 'requirements.txt'],
            ['python', '-m', 'pip3', 'install', '-r', 'requirements.txt'],
            ['python3', '-m', 'pip', 'install', '-r', 'requirements.txt'],
            ['python3', '-m', 'pip3', 'install', '-r', 'requirements.txt']
        )
    # Linux
    else:
        commands = (
            ['pip', 'install', '-r', 'requirements.txt'],
            ['pip3', 'install', '-r', 'requirements.txt'],
        )

    # Install python packages
    print('Installing required packages.')
    for command in commands:
        try:
            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, shell=True, timeout=60,
                universal_newlines=True)
        except subprocess.CalledProcessError:
            pass
        else:
            print(output)

    # Setup the database
    username = input('Database username: ')
    password = getpass('Database password: ')

    command = 'mysql --user="{}" --password="{}" --execute="source PayrollManagementDatabase.sql"'.format(
        username, password)
    print('Setting up database.')
    os.system(command)


