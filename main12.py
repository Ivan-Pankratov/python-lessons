print("Программа находит пару чисел по значениям их суммы и произведения.")
sumNumbers = int(input("Введите сумму искомых чисел: "))
productNumbers = int(input("Введите произведение искомых чисел: "))
k = 0
i = 0
while i <= sumNumbers and k == 0:
    for j in range(productNumbers+1):
        if sumNumbers == i + j and productNumbers == i * j:
            print(i, j)
            k +=1
    i+=1
if k == 0:
    print("Таких пар чисел нет")