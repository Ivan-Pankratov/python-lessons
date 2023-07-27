def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


n = int(input("Введите номер числа Фибоначчи: "))
print(fib(n))
# 0 1 1 2 3 5 8 13 21 34 55 89
# 0 1 2 3 4 5 6 7  8  9