from functools import wraps
from logging import getLogger, basicConfig, INFO, WARNING, DEBUG


def configure_loggers():
    basicConfig()
    root = getLogger('App')
    root.setLevel(WARNING)
    user = root.getChild('User')
    user.setLevel(INFO)

def log_user_selection(selection):
    # prints 'Selected : Hello' to User log
    getLogger('App.User').info('Selected ' + repr(selection))


def _log_result(func, log_func):
    """
        Used as a decorator for func. func's return value will be logged using log_func.

    :param func: the function being decorated whose return value will be logged with log_func
    :param log_func: the callable that is used to perform logging
    :return: a function
    """

    @wraps(func)  # this is used to preserve func's metadata after wrapping
    def wrapper_logit(*args, **kwargs):
        original_return_value = func(*args, **kwargs)
        log_func(original_return_value)
        return original_return_value

    return wrapper_logit


def log_result_with(log_func):
    """
        Decorates a function by taking the return value of that func and logging it with log_func param

        :param log_func: a logging function to record the return value of the decorated function.
        :return: a function

        Example Usages
        #Bespoke Logging Function
        @log_results_with(my_log_function): ...
        def some_func(params)

        #using builtin logging module
        @log_results_with(logging.error)
        def some_func(params): ...

        #plain old print
        @log_results_with(print)
        def some_func(params): ...

        Expected Behaviour:
        @log_results_with(logging.error)
        def get_two(): return 2
        >>> x = get_two()
        ERROR:root:2
        >>> print(x)
        2
        """

    return lambda func: _log_result(func, log_func)


def my_log(x):
    print(f'logging - {x} - was returned!')


@log_result_with(my_log)
def greeting(name):
    '''original documentation'''
    return f'hello {name}'


x = greeting('monty')
print('at long last,', x)
print(greeting.__doc__)
