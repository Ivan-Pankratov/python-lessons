

# Заполнение списка, где длина задаётся пользователем, а элементы через рандом.
# import random
from random import randint as rd # alias (псевдоним)
print("Программа находит самый близкий элемент в списке к искомому.")
n = int(input("Введите количество элементов в списке: "))
list_1 = list()
for i in range(n):
    list_1.append(rd(0, 10))
print(list_1)
k = int(input("Введите искомое число: "))
x= abs(list_1[0] - k)
result = list_1[0]
for i in range (len(list_1)):
    d = abs(list_1[i] -k)
    if d<x:
        x =d
        result = list_1[i]
print(result)