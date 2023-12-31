#  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def summary (a : int):
    if a == 1 :
        print("Стих получился!")
        print("Парам пам-пам")
    else:
        print("Не стих")
        print("Пум пурум")

def number(word: str):
    result = 0
    lit = ("а", "у", "е", "ы", 'о', 'э', 'я', 'и', 'ю', 'ё')
    word = word.lower()
    for elem in lit:
        result += word.count(elem)
    return result

st = input("Введите стишок Винни-пуха: ")
poem = st.split( )
count1 = 1
n = number(poem[0])
for elem in range(len(poem)):
    if n != number(poem[elem]): count1 += 1
summary(count1) 

