import time
from functools import wraps


# Декоратор для измерения времени выполнения
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"{func.__name__}({args}, {kwargs}) = {result}, "
              f"выполнено за {elapsed:.8f} секунд")
        return result

    return wrapper


# Чистая рекурсивная функция факториала (без декоратора)
def recursion_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n - 1)


# Итеративная версия факториала (без декоратора)
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Оборачиваем только внешние вызовы
timed_recursion_factorial = timing_decorator(recursion_factorial)
timed_iterative_factorial = timing_decorator(iterative_factorial)

# Примеры вызова — будет ровно 6 строк вывода
timed_recursion_factorial(3)
timed_iterative_factorial(3)

timed_recursion_factorial(10)
timed_iterative_factorial(10)

timed_recursion_factorial(30)
timed_iterative_factorial(30)
