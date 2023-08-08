text = input("Введите текст: ").split()
count_char = {}
for char in text:
    if char not in count_char:
        print(char, end=" ")
        count_char[char] = 1
    else:
        print(f'{char}_{count_char[char]}', end=' ')
        count_char[char] += 1