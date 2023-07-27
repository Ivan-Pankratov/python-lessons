

def sum(a, b):
    if b == 0:
        result = a
    else:
        result = sum (a, b-1)+1
    return result


a = int(input("Введите целое число: "))
b = int(input("Введите второе число: "))
print ( sum(a, b))