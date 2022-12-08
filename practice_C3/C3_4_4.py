import os

with open("input.txt", 'r') as f:
    with open("output.txt", 'a') as g:
     for line in f:
         g.writelines(line)