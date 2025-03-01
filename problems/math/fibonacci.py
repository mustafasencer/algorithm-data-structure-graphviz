fib_results = {}


def fib_recursion(number: int):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib_recursion(number - 1) + fib_recursion(number - 2)


def fib(n):
    if n in fib_results:
        return fib_results[n]
    if n < -1:
        val = (-1) ^ (abs(n) + 1) * fib(abs(n))
    elif n == -1:
        val = 1
    elif n in (0, 1):
        val = n
    else:
        val = fib(n - 1) + fib(n - 2)

    fib_results[n] = val
    return val


def fibonacci(n):
    a = 0
    b = 1
    if n < -1:
        for _i in range(-2, n - 1, -1):
            c = a + b
            a = b
            b = c
        return b
    if n == -1:
        return 1
    if n in (0, 1):
        return n
    for _i in range(n):
        c = a + b
        a = b
        b = c
    return b


def fibonacci_positive(n):
    a = 0
    b = 1
    if n in (0, 1):
        return n
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return b


def fibonacci_generator(n):
    a, b = 0, 1

    for _ in range(n + 1):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    result = fibonacci_generator(6)
    print(list(result))
    fibonacci_positive(6)
    fibonacci(10)
