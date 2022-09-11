# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
n = int(input('Enter a number: '))
temp_list = []
for i in range (-n, n):
    temp_list.append((random.randint(-n, n)))
print(temp_list)
temp = open('file.txt', 'r')
multiply = 1
for i in temp.readlines():
    multiply *= temp_list[int(i)]
print(multiply)