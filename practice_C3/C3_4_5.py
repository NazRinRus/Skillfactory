import os

with open("numbers.txt", 'r') as f:
    min_num = max_num = int(f.readline())
    for line in f:
         if min_num > int(line):
             min_num = int(line)
         if max_num < int(line):
             max_num = int(line)

print("max: ", max_num, "min: ", min_num, "sum: ", min_num + max_num)

with open("output.txt", 'a') as f:
    f.writelines("Сумма максимального и минимального значений: " + str(min_num + max_num))