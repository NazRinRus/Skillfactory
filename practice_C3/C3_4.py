import os

f = open('numbers.txt', 'w', encoding='utf8')

# Запишем в файл строку
f.write("6\n")
f.write("9\n")
f.write("3\n")
f.write("5\n")
f.write("2\n")
f.write("10\n")
f.write("1\n")
f.write("4\n")
# обязательно нужно закрыть, файл иначе он будет заблокирован ОС
f.close()

f = open('test.txt', 'r', encoding='utf8')
print(f.read(10))  # This is a
# считали остаток файла
print(f.read())  # test string\nThis is a new string\n
# обязательно закрываем файл
f.close()

f = open('test.txt', 'a', encoding='utf8')  # открываем файл на дозапись

sequence = ["other string\n", "123\n", "test test\n"]
f.writelines(sequence)  # берёт строки из sequence и записывает в файл (без переносов)

f.close()

f = open('test.txt', 'r', encoding='utf8')

print(f.readlines())  # считывает все строки в список и возвращает список

f.close()

f = open('test.txt', 'r', encoding='utf8')

print(f.readline())  # This is a test string
print(f.read(4))  # This
print(f.readline())  # is a new string

f.close()

f = open('test.txt')  # можно перечислять строки в файле
for line in f:
    print(line, end='')

# This is a test string
# This is a new string
# other string
# 123
# test test

f.close()

# В блоке менеджера контекста открытый файл «жив» и с ним можно работать, при выходе из блока файл закрывается.
with open("test.txt", 'rb') as f:
    a = f.read(10)
    b = f.read(23)

