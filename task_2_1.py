# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Enter a number: ')
sum_number = 0
for i in number:
    if i != ".":
        sum_number += int(i)
print(f'{number} -> {sum_number}')
