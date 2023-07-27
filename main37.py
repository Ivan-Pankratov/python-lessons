
def print_number(n):
    if n == 0:
        return ''
    k = input("Введите число: ")
    return print_number(n - 1) + f' {k}'


n = int(input("Введите кол-во чисел: "))
print(print_number(n))