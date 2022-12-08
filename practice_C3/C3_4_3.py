import os

path_a = input("Введите путь к папке: ")
def info_dir(path = os.getcwd()):
    if path == '':
        path = os.getcwd()
    print("Информация о папке с путем: ", path)
    tree = os.walk(path)
    for path_dir, name_dir, name_file in tree:
        print("Содержимое папки: ", path_dir)
        print("Папки: ")
        for i in name_dir:
            print(i)
        print("Файлы: ")
        for j in name_file:
            print(j)

info_dir(path_a)




