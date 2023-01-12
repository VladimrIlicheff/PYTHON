# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# in 54 out [2, 3, 3, 3]
# in 9990 out [2, 3, 3, 3, 5, 37]
# in 650 out [2, 5, 5, 13]

num = int(input("Введите любое число:  "))
count = 2
my_list = []
while num > 1:
    if num % count == 0:
        my_list.append(count)
        num = num / count
    else: 
        count += 1
print (my_list)