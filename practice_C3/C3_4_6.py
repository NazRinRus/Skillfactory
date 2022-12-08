import os

with open('input2.txt', encoding="utf8") as file:
    for line in file:
        points = int(line.split()[-1])
        if points < 3:
            name = " ".join(line.split()[:-1])
            print(name)