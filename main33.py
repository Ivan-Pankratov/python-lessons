# from random import randint as rd # alias (псевдоним)
# # заполнение журнала Василия
# n = int(input("Введите количество элементов в списке: "))
# data_list = list()
# for i in range(n):
#     data_list.append(rd(1, 5))
# print(data_list)

# max = data_list[0]
# min = data_list[0]
# for i in range (n):
    
#     if data_list[i] > max:
#         max_massa = data_list[i]
#     elif data_list[i] < min:
#         min_massa = data_list[i]


from random import randint as rd


n = int(input("Введите кол-во оценок: "))
marks = []
for i in range(n):
    marks.append(rd(1, 5))
print(marks)
min_mark = min(marks)
max_mark = max(marks)
for i in range(n):
    if marks[i] == max_mark:
        marks[i] = min_mark
print(*marks)