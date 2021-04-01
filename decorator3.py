def check_password(func):
    access_password = '123'

    def wrapper(*args, **kwargs):
        print('Введите пароль:')
        password = input()
        if password == access_password:
            return func(*args, **kwargs)
        print('В доступе отказано')
    return wrapper


@check_password
def show_grades():
    return '7, 6, 2'


print(show_grades())
