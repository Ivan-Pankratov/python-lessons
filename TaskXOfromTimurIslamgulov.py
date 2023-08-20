# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например,

# |     |  Х | 
# |     |  O |
# |     |  O |

def print_line(line: list):                             # функция печати строки
    for i in range (len(line)):
        print('|', line[i], end="")
    print("|")

def print_field(field: list):                           # функция печати игрового поля
    for i in range (len(field)):
        print_line(field[i])
    
def check_free(x: int, y : int, field : list):          # функция проверки свободно ли поле
    if field[x][y] == " ":
        return True
    return False

def check_forth(field: list):                           # функция проверки свободных ячеек
    set1 = set(field[0]) 
    set1 = set1.union(set(field[1]))
    set1 = set1.union(set(field[2]))
    if (" " in set1) :
        return True
    return False

def motion1(field: list):                               # функция хода соперника
    st=1
    while st == 1 :
        x = int(input("Введите номер строки, куда ходите: "))-1
        y = int(input("Введите номер столбца, куда ходите: "))-1
        if check_free(x, y, field): 
            return x, y
        else :
            print("Это поле уже занято. Прошу сходить иначе.")

def motion2(field: list, x: int, y: int):               # функция хода бота (использована рекурсия)
    if check_forth(field):
        while not(check_free(x, y, field)):
            if check_forth(field[x]):
                if check_free(x, y-1, field): 
                    y = y-1
                else:
                    y = y-2
            elif check_forth(field[x-1]):
                x=x-1
                x, y = motion2(field, x, y)
            elif check_forth(field[x-2]):
                x=x-2
                x, y = motion2(field, x, y)
    else:
        print("У меня нет вариантов для хода.")
        print_field(field)
        quit()
       
    return x, y

            
def change(x: int, y: int, field: list, elem: str):     # функция замены символа в поле
    z = list(field[x])
    z[y] = elem
    field[x]=tuple(z)
    return field

def winner(field: list):                                # функция останавливает игру и объявляет победителя
    set1 = {}
    for i in range(3):
        set1 = set(field[i])
        if set1 == {"x"}: 
            print("Ты победил!")
            quit()
        elif set1 == {"0"}: 
            print("Победил бот, но у тебя тоже отличный результат.")
            quit()
        

print("Сыграем в крестики-нолики?")                 # начало, приглашение в игру
answer = input("Что ответишь, да/нет? ")
if answer in {"да", "Да", "yes", "ok", "+", "Yes", 'Ok'}:
    print("Отлично! Твой крестик, ходи!")
    st = 1
else :
    print("Как знаешь.")                            # прерывание в случае отказа  
    quit()
line0 = (" ", " ", " ")                             # задание игрового поля
field = [line0 for i in range(3)]
print_field(field)
bot_row, bot_column = 1, 1                          # предзадание хода бота 
while check_forth(field):

    x, y = motion1(field)                               # вызов хода соперника
    field = change(x, y, field, "x")   
    bot_row, bot_column = motion2(field, bot_row, bot_column)                 # вставка хода в поле
    field = change(bot_row, bot_column, field, "0")                   # вставка в поле хода бота
    print_field(field)
    winner(field)

print()
print_field(field)