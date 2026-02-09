# Нужно создать три уровня вложенности: внешний принимает аргументы декоратора, средний — функцию,
# внутренний — аргументы функции.

# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                print(f"Запуск {i + 1}/{times} функции {func.__name__}")
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Привет, {name}!")


greet("Миша")
