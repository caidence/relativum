class InvalidTableNameError(Exception):
    def __init__(self, message):
        super().__init__(message)


class RequirementsNotMetError(Exception):
    def __init__(self, message):
        super().__init__(message)


class AuthenticationError(Exception):
    """Generic authentication error.
    """
    def __init__(self, message):
        super().__init__(message)