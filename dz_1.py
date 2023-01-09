# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).
# in 5 out [10, 2, 3, 8, 9]    22

# in 4 out [4, 2, 4, 9]   8

from random import sample
number = int(input("Ведите количество чисел:  "))
num_list = sample(range(1, number * 3), k=number)
print(num_list)
new_list = num_list[::2]
print (sum(new_list))


