# Это функция, которая принимает другую функцию и расширяет её поведение, не меняя исходный код. Часто используется
# для логирования, кэширования или проверки прав доступа.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def adder(*args):
    return sum(args)


# Просто вызываем adder
print(adder(1, 2, 3))  # Вызов adder -> 6
