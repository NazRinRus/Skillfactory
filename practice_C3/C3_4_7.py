import os

with open('input.txt', 'r') as input_file:
   with open('output.txt', 'w') as output_file:
       for line in reversed(input_file.readlines()):
           output_file.write(line)