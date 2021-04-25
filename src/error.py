class InvalidTableNameError(Exception):
    """Table not found for SQL query."""
    def __init__(self, message):
        super().__init__(message)


class RequirementsNotMetError(Exception):
    """For SQL INSERT, missing table attributes."""
    def __init__(self, message):
        super().__init__(message)


class TooManyArguments(Exception):
    """Used for SQL remove, only one argument should be specified"""
    def __init__(self, message):
        super().__init__(message)


class AuthenticationError(Exception):
    """Generic authentication error."""
    def __init__(self, message):
        super().__init__(message)