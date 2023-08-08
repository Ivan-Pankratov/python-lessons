print("Программа находит максимальную сумму тройки соседних элементов, расположенных в кольце.")
n = int(input("Введите количество элементов в 1 наборе: "))
list_1 = list()
for i in range(n):
    list_1.append(int(input("Введите целое число: ")))
char_max = list_1[0]+list_1[1]+list_1[2]
for i in range(n):
    if i == 0:
        s = list_1[i]+list_1[i+1]+list_1[n-1]
    elif i == n-1:
        s = list_1[i]+list_1[i-1]+list_1[0]
    else: 
        s = list_1[i]+list_1[i-1]+list_1[i+1]
    if s > char_max:
        char_max = s
print(char_max)

