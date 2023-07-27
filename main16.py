# Заполнение списка, где длина задаётся пользователем, а элементы через рандом.
# import random
from random import randint as rd # alias (псевдоним)

n = int(input("Введите количество элементов в списке: "))
data_list = list()
for i in range(n):
    data_list.append(rd(0, 10))
print(data_list)