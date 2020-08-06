from functools import wraps
from logging import getLogger, basicConfig, INFO


# Decorator Function intended to take a result of func, and then execute a logging function on it,
def log_result(func, log_func):
    """

    :param func: some function or callable being decorated, whose result shall be logged.
    :param log_func: a callback to a logging function which is intended to log the return value func parameter.
    :return: internal wrapper function
    """
    @wraps(func)
    def wrapper():
        original_return_value = func()
        log_func(original_return_value)
        return original_return_value

    return wrapper


def configure_logger():
    basicConfig(level=INFO)


def log_user_selection(selection):
    # prints 'Selected : Hello' to User log
    getLogger('User').info('Selected : ' + str(selection))
