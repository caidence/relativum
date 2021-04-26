class RequirementsNotMetError(Exception):
    """For SQL INSERT, missing table attributes."""
    def __init__(self, message):
        super().__init__(message)


class AuthenticationError(Exception):
    """Generic authentication error."""
    def __init__(self, message):
        super().__init__(message)
