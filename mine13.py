print("Программа находит продолжительность самой долгой оттепели.")
n = int(input("Введите продолжительность рассматриваемого периода: "))
print ("Введите среднесуточную температуру в каждый день периода: ")
count = 0
result = 0
for i in range (n):
    x = int(input())
    if x > 0:
        count +=1
        if result < count:
            result = count
    else:
        count = 0
print (result)
    
