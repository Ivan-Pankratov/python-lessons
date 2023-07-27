# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
from random import randint as rd # alias (псевдоним)

n = int(input("Введите количество элементов в списке: "))
data_list = list()
for i in range(n):
    data_list.append(rd(0, 10))
print(data_list)


step = int (input("введите количество сдвигов: "))
step = step % len(data_list)
result_list = data_list
for i in range(len(data_list)):
    result_list[i] = data_list[i - step] 
print (result_list)
