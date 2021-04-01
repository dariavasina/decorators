def time_spent(func):
    import time

    def wrapper():
        start = time.time()
        res = func()
        end = time.time()
        print('Время выполнения функции func - ', end - start, 'с')
        return res
    return wrapper


@time_spent
def func():
    import requests
    requests.get('http://google.com/')

func()
