from error import RequirementsNotMetError


def add_helper(cursor, arguments, required_arguments, table_name):
    """Helper function to handle table insert commands.

    :param cursor: Cursor for SQL command execution.
    :param arguments: All arguments passed to program.
    :param required_arguments: Required arguments to add row to table.
    :param table_name: Table to run add statement against.
    """
    __validate_command(arguments, required=required_arguments)
    columns = str()
    value_placeholders = str()

    for k, v in vars(arguments).items():
        if k == required_arguments[-1]:  # Don't want a comma after the last value
            columns += k
            value_placeholders += '?'
        elif k in required_arguments:
            columns += k + ','
            value_placeholders += '?,'
    sql = 'INSERT INTO {} ({}) VALUES ({})'.format(table_name, columns, value_placeholders)

    # __get_argument_list returns a list of two-item-tuples; we only need the second item of each here
    values = tuple([x[1] for x in __get_argument_list(arguments, required_arguments)])
    cursor.execute(sql, values)


def update_helper(cursor, arguments, valid_arguments, update_arguments, table_name):
    """Helper function to handle table update commands.

    :param cursor: Cursor for SQL command execution.
    :param arguments: All arguments passed to program.
    :param valid_arguments: Tuple of valid column names to run a remove statement on.
    :param update_arguments: Valid columns in table that may be updated.
    :param table_name: Table to run remove statement against.
    """
    __validate_command(arguments, valid=valid_arguments, update=update_arguments)
    update_params = __get_argument_list(arguments, update_arguments)
    search_params = __get_argument_list(arguments, valid_arguments)

    # TODO: This can be simplified
    for index, param in enumerate(update_params):
        sql = 'UPDATE {} SET {}=? WHERE {} like ?'.format(
            table_name, __remove_string_front(4, param[0]), search_params[index][0])
        values = (vars(arguments)[param[0]], search_params[index][1])
        cursor.execute(sql, values)


def remove_helper(cursor, arguments, valid_arguments, table_name):
    """Helper function to remove rows from tables.

    :param cursor: Cursor for SQL command execution.
    :param arguments: All arguments passed to program.
    :param valid_arguments: Tuple of valid column names to run a remove statement on.
    :param table_name: Table to run remove statement against.
    """
    # Make sure one of these arguments were passed to the program
    __validate_command(arguments, valid=valid_arguments)
    search_params = __get_argument_list(arguments, valid_arguments)

    # TODO: allow multiple search constraints or throw error if more than one is passed
    sql = 'DELETE FROM {} WHERE {} like ?'.format(table_name, search_params[0][0])
    values = (search_params[0][1],)
    cursor.execute(sql, values)


def __validate_command(arguments, required=tuple(), valid=tuple(), update=tuple()):
    """Helper function to validate arguments passed to command line fit function being called.

    :param arguments: All arguments passed to the command line.
    :param required: List of required arguments for add functionality.
    :param valid: List of valid arguments for remove functionality.
    :param update: List of updatable arguments for update functionality.
    """
    global_argument_dict = vars(arguments)

    # For insert statements
    if len(required) > 0:
        requirements_not_met = [arg for arg in required if global_argument_dict[arg] is None]
        if len(requirements_not_met) != 0:
            msg = 'The following arguments are missing: {}'.format(requirements_not_met)
            raise RequirementsNotMetError(msg)

    # For remove functionality
    if len(valid) > 0:
        valid_not_used = [arg for arg in valid if global_argument_dict[arg] is not None]
        if len(valid_not_used) == 0:
            msg = 'Pleas provide only ANY of the following arguments: {}'.format(valid)
            raise RequirementsNotMetError(msg)

    # For update functionality
    if len(update) > 0:
        total_valid_update = [arg for arg in update if global_argument_dict[arg] is not None]
        if len(total_valid_update) == 0:
            msg = 'Pleas provide only ANY of the following arguments: {}'.format(update)
            raise RequirementsNotMetError(msg)


def __get_argument_list(arguments, in_constraints: tuple = tuple()) -> list:
    """Get a list of tuples of the key-value paris from the argument dictionary if it is in the constraint list.

    :param arguments: All arguments passed to the command line.
    :param in_constraints: Tuple of strings to make sure arguments is in.
    """
    global_argument_dictionary = vars(arguments)

    # Get non-null arguments that are in the constraints list
    if len(in_constraints) > 0:
        return [(k, v) for k, v in global_argument_dictionary.items() if k in in_constraints and v is not None]
    return [(k, v) for k, v in global_argument_dictionary.items() if v is not None]


def __remove_string_front(index, string):
    """Helper function to cleanup update_helper and improve readability.

    Remove the first [index] characters of a string.

    :param index: Number of characters to remove from front of string.
    :param string: String to remove characters from.
    :return: string with first [index] characters removed
    """
    return string[index:]
