# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
from random import randint as rd # alias (псевдоним)

n = int(input("Введите количество элементов в списке: "))
data_list = list()
for i in range(n):
    data_list.append(rd(0, 10))
print(data_list)

m = set (data_list)
print (len(m))