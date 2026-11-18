import functools
import sys


def log(filename=None):
    """Автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def write_log(msg):
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg + "\n")
                else:
                    sys.stdout.write(msg + "\n")

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                write_log(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise e
            else:
                write_log(f"{func.__name__} ok")
                return result
        return wrapper
    return decorator
