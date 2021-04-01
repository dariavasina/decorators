def check_password(func):
    access_password = '123'

    def wrapper(*args, **kwargs):
        print('Введите пароль:')
        password = input()
        if password == access_password:
            return func(*args, **kwargs)
        print('В доступе отказано')

    return wrapper


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


@check_password
def fib1(n):
    print(fib(n))


#fib1(10)