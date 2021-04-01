def make_upper(func):
    def wrapper(*args, **kwargs):
        new_args = [str(arg).upper() for arg in args]
        return func(*new_args, **kwargs)

    return wrapper


print = make_upper(print)
print('a', 'b', 'c', 1)