#  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

operation1 = lambda x, y: x*y
operation2 = lambda x, y: x+y
operation3 = lambda x, y: x**y

def print_operation_table(operation, x, y):
    for i in range(x):
        for j in range(y):
            d = str(operation(i+1, j+1))
            print(d.ljust(5), end = " " )
        print(" ")


x=10
y=3
print_operation_table(operation1, x, y)
# print()
# print_operation_table(operation2, x, y)
# print()
# print_operation_table(operation3, x, y)
    