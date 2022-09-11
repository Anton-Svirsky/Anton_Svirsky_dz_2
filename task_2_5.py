# Реализуйте алгоритм перемешивания списка.

import random
temp_list = [random.randint(0, 10)]
for i in range(0, 10):
    temp_list.append(i)
print(temp_list)
random.shuffle(temp_list)
print(temp_list)
