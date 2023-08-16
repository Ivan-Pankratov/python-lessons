# sp = [1, 2, 3, 5, 8, 15, 23, 38]
# print([(item, item**2) for item in sp if item%2 ==0])

# задача 47
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# def trasformation(l : list):
#     return l

# trasformation = lambda val : val

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:



# def find_planets(list_of_orbits: list):
#     list1 = list()
#     for char in list_of_orbits :
#         if char[0]!= char[1]:
#             list1 = list.append(char)
#     return list1
def sq (char: tuple) :
    if char[0]!=char[1]: return (char[0]*char[1])
    return 0                       # = lambda char:  char[0]*char[1] if char[0]!=char[1]: char[0]*char[1]


def find_farthest_orbit(list_of_orbits: list):
    #list_of_orbits = find_planets(list_of_orbits)
   
    result = list_of_orbits[0]
    for char in set(list_of_orbits):
        if sq(char) > sq(result):
            result = char
    return result

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))

