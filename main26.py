# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def f(a, b):
    if a == 0:
        result = 0
    else:
        result = 1
        i=1 
        while i <= b:
            result *= a
            i += 1
    return result


a = int(input("Введите целое число: "))
b = int(input("Введите показатель степени, второе число: "))
print ( f(a, b))