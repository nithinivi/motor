import logging
import time
from functools import wraps, partial


def timeDebug(func):
    """
    Decorator that reports the time of exccution

    """

    #    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


def funcDebug(func=None,*, prefix=''):
    """Decorator that prints msg when code is excuted
    """
    if func is None:
        return partial(funcDebug, prefix=prefix)
    msg = prefix + func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)

    return wrapper


def logged(level, name=None, msg=None):
    """Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = msg if msg else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            print(logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


if __name__ == '__main__':

    #    @timeDebug
    #    @logged(logging.DEBUG)
    @funcDebug(prefix="nh")
    def add1(a, b):
        return a + b

    add1(10, 10)
