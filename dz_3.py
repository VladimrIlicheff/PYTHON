# 3. Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной 
#  последовательности в том же порядке.
# in 7 out [4, 5, 3, 3, 4, 1, 2]    [5, 1, 2]
# in -1 out Negative value of the number of numbers! []
# in 10 out [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]   [6, 2, 3, 0, 9]

import random 
number = int(input("Введите длинну последовательности:  "))
if number <= 0:
    print ("Negative value of the number of numbers!")
list_source = [random.randrange(1, 15, 1) for i in range(number)]
print (list_source)
list_final = []
def get_unique(list_source):
   for i in list_source:
    if list_source.count (i) == 1:
        list_final.append(i)
get_unique(list_source)
print(list_final)

