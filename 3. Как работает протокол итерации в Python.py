# При вызове цикла for Python вызывает iter(obj). Полученный итератор вызывается через next() до тех пор,
# пока не возникнет исключение StopIteration.


# Вот три варианта одного и того же обхода списка `[10, 20, 30]`:

### 1️⃣ Обычный цикл `for`

numbers = [10, 20, 30]

for num in numbers:
    print(num)


### 2️⃣ Явная работа с протоколом итерации (`iter` + `next`)

numbers = [10, 20, 30]

iterator = iter(numbers)   # получаем итератор

while True:
    try:
        num = next(iterator)   # берём следующий элемент
        print(num)
    except StopIteration:
        break   # когда элементы закончились, выходим из цикла


### 3️⃣ Генератор с `yield`

def my_generator():
    yield 10
    yield 20
    yield 30

for num in my_generator():
    print(num)
