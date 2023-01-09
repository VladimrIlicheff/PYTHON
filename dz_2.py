# 2. Напишите программу, которая найдёт произведение пар 
# чисел списка.Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# in 4 out [2, 5, 8, 10]
# [20, 40]

# in 5 out [2, 2, 4, 8, 8]
# [16, 16, 4]
from random import sample
number = int(input("Ведите количество чисел:  "))
num_list = sample(range(1, number * 3), k=number)
print(num_list)
new_list = list(reversed(num_list))
result_list = []
if (number % 2) == 0: 
    for i in range(0,len(num_list)): 
      result_list.append(num_list[i]*new_list[i])
    print(result_list) 
else:
    for i in range(0,len(num_list)):
       result_list.append(num_list[i]*new_list[i])
    result_list[number//2] = (num_list[(number-1)//2])
    print(result_list)

