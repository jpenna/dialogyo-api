class DyoError(Exception):
    "Custom application error class"
    pass


class ApiError(DyoError):
    """Custom error class raised for API errors.

    Attributes:
        code    -- Code umber specific for this error
        type    -- Category for the error
        message -- Explanation of the error
    """

    def __init__(self, code, type_, message):
        self.code = code
        self.type = type_
        self.message = message
