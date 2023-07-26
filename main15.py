print("Программа находит вес самого тяжёлого и самого легкого арбуза.")
n = int(input("Введите количество арбузов: "))
x = int(input("Введите массу арбуза: "))
min_massa, max_massa = x, x
for i in range (n-1):
    x = int(input("Введите массу арбуза: "))
    if x > max_massa:
        max_massa = x
    elif x < min_massa:
        min_massa = x
print(f'Масса самого тяжёлого арбуза {max_massa} кг, а масса самого легкого арбуза {min_massa} кг.')