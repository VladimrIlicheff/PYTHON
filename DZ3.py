# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

num_list = []
sum = 0
n = int (input ('Введите длину списка '))
for n in range (1, n+1):
   num = (1 + 1/n) ** n 
   num_list.append (round(num,3))
   sum = sum + num 
print (num_list)
print (round(sum))
