# 3. Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной 
#  последовательности в том же порядке.
# in 7 out [4, 5, 3, 3, 4, 1, 2]    [5, 1, 2]
# in -1 out Negative value of the number of numbers! []
# in 10 out [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]   [6, 2, 3, 0, 9]

import random 
number = int(input("Введите длинну последовательности:  "))
list_source = [random.randrange(1, 15, 1) for i in range(number)]
print (list_source)
def get_unique(list_source):
   list_final = []
   for x in list_source:
      if x not in list_final:
        list_final.append(x)
   for x in list_final:
      print(x)
get_unique(list_source)

