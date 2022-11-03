# Объявление таблицы - игровое поле
playing_field = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

# Функция вывода таблицы
def print_playing_field(table1):
    print("Игровое поле:")
    print("____________")
    print("   0  1  2")
    for i in range(3):
        str1 = str(i) + " | "
        for j in range(3):
            if table1[i][j] != '': # добавлять или нет пробел, чтоб таблица не съезжала
                str1 += table1[i][j] + "| "
            else:
                str1 += table1[i][j] + " | "
        print(str1)

# Функция ввода пользователя
def input_playing_field(table1):
    print('Выберите ячейку (номер строки, номер столбца)')
    x = int(input('Введите номер строки: '))
    y = int(input('Введите номер столбца: '))
    if table1[x][y] == '':
        table1[x][y] = 'x'
    else:
        print('данная ячейка занята')

# Функция проверки условий победы
def victory_conditions(table1, x_or_0='x'):
    win = False
    column1 = []
    diagonal1 = []
    diagonal2 = []
    for i in range(3): #проверка по строкам
        if table1[i].count(x_or_0) == 3:
            win = True
    for i in range(3):  # проверка по столбцам
        for j in range(3):
            column1.insert(j, table1[j][i])
        if column1.count(x_or_0) == 3:
            win = True
        column1 = []
    for i in range(3): #проверка по диагоналям
        diagonal1.insert(i, table1[i][i])
        diagonal2.insert(i, table1[i][2 - i])
    if diagonal1.count(x_or_0) == 3:
        win = True
    elif diagonal2.count(x_or_0) == 3:
        win = True
    return win

#Проверка наличия пустых полей
def empty_fields(table1):
    empty_field = False
    for i in range(3): #проверка по строкам
        if table1[i].count(''):
            empty_field = True
    return empty_field

# Ход компьютера
def computer_running1(table1):
    content_str = []# будет заполняться поочередно содержимым строк, столбцов и диагоналями
    running_bool = False #индикатор хода компьтера
# проверка на выигрышную ситауцию - наличие в одной строке, столбце, диагонали 2 ноликов
    for i in range(3):
        for j in range(3):
            content_str.insert(j, table1[i][j])
        if (content_str.count('0') == 2) and (content_str.count('')) and (running_bool == False):
            table1[i][content_str.index('')] = '0'
            running_bool = True
        content_str = []
        for j in range(3):
            content_str.insert(j, table1[j][i])
        if (content_str.count('0') == 2) and (content_str.count('')) and (running_bool == False):
            table1[content_str.index('')][i] = '0'
            running_bool = True
        content_str = []
    for j in range(3):
        content_str.insert(j, table1[j][j])
    if (content_str.count('0') == 2) and (content_str.count('')) and (running_bool == False):
        table1[content_str.index('')][content_str.index('')] = '0'
        running_bool = True
    content_str = []
    for j in range(3):
        content_str.insert(j, table1[j][2 - j])
    if (content_str.count('0') == 2) and (content_str.count('')) and (running_bool == False):
        table1[content_str.index('')][2 - content_str.index('')] = '0'
        running_bool = True
    content_str = []

# проверка на потенциально проигрышную ситауцию - наличие в одной строке, столбце, диагонали 2 крестиков
    for i in range(3):
        for j in range(3):
            content_str.insert(j, table1[i][j])
        if (content_str.count('x') == 2) and (content_str.count('')) and (running_bool == False):
            table1[i][content_str.index('')] = '0'
            running_bool = True
        content_str = []
        for j in range(3):
            content_str.insert(j, table1[j][i])
        if (content_str.count('x') == 2) and (content_str.count('')) and (running_bool == False):
            table1[content_str.index('')][i] = '0'
            running_bool = True
        content_str = []
    for j in range(3):
        content_str.insert(j, table1[j][j])
    if (content_str.count('x') == 2) and (content_str.count('')) and (running_bool == False):
        table1[content_str.index('')][content_str.index('')] = '0'
        running_bool = True
    content_str = []
    for j in range(3):
        content_str.insert(j, table1[j][2 - j])
    if (content_str.count('x') == 2) and (content_str.count('')) and (running_bool == False):
        table1[content_str.index('')][2 - content_str.index('')] = '0'
        running_bool = True
    content_str = []

#Если нет потенциально проигрышной ситуации, то ставим 0 в первом не занятом поле
    if running_bool == False:
        for i in range(3):
            for j in range(3):
                content_str.insert(j, table1[i][j])
            if (running_bool == False) and (content_str.count('')):
                table1[i][content_str.index('')] = '0'
                running_bool = True
            content_str = []
    return table1

gamover = False
while gamover == False:
    print(print_playing_field(playing_field))
    if empty_fields(playing_field):
        input_playing_field(playing_field)
    else:
        input('Ничья. Пустых полей нет. Нажмите Enter для выхода')
        break
    print(print_playing_field(playing_field))
    gamover = victory_conditions(playing_field, 'x')
    if gamover:
        input('Поздравляю! Вы победили! нажмите Enter для выхода')
        break
    if empty_fields(playing_field):
        computer_running1(playing_field)
    else:
        input('Ничья. Пустых полей нет. Нажмите Enter для выхода')
        break
    gamover = victory_conditions(playing_field, '0')
    if gamover:
        print(print_playing_field(playing_field))
        input('Вы проиграли! нажмите Enter для выхода')
        break

