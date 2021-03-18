"""
    authentication tools
"""


def check_perm(perm_name: str):

    def decorator(func):

        def inner(*args, **kwargs):
            pass

            return func(*args, **kwargs)
        return inner
    return decorator
