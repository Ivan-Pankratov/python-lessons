# проверяем, простое ли число введено
n = int(input("Введите число: "))
count_del = 0
i = 2
while count_del == 0 and i <= n // 2:
    if n % i == 0:
        count_del += 1
    i += 1
print("yes" if count_del == 0 else "no")