from app_errors import ApiError


def error_formatter(error, debug: bool = False) -> dict:
    """Format ApiError message with:
        code -- Code number for the error
        type -- Category of the error
        message -- Description of the error
    """

    formatted = error.formatted
    original_error = error.original_error
    if isinstance(original_error.original_error, ApiError):
        code, type_, message = original_error.original_error.args
        formatted["message"] = dict(code=code, type=type_, message=message)
    return formatted
