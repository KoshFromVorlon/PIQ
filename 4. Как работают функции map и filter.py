# map(func, iterable) применяет функцию к каждому элементу. filter(func, iterable) оставляет только те элементы,
# для которых функция вернула True. Оба возвращают итераторы.

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))  # [1, 4, 9, 16]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
