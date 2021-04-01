def cached(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        res = cache[n] = func(n)
        return res
    return wrapper


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


#print(fib(100))