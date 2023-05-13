from typing import Callable

add: Callable[[int, int], int] = lambda x, y: x + y
subtract: Callable[[int, int], int] = lambda x, y: x - y
multiply: Callable[[int, int], int] = lambda x, y: x * y


def calc(num1: int, num2: int, operation: Callable[[int, int], int]) -> int:
    return operation(num1, num2)


print(add)
print(hex(id(add)))
print(calc(10, 9, add))
