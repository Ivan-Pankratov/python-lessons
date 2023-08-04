# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N].

# Заполнение списка, где длина задаётся пользователем, а элементы через рандом.
# import random
from random import randint as rd # alias (псевдоним)

n = int(input("Введите количество элементов в списке: "))
list_1 = list()
for i in range(n):
    list_1.append(rd(0, 10))
print(list_1)
k = int(input("Введите искомое число: "))
x=0
for i in range (len(list_1)):
    if k == list_1[i]:
        x +=1
print(x)